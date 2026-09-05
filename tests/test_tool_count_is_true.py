"""The number this server tells clients must be the number it serves.

server.py advertised "59 compliance tools in one MCP server" in its `instructions` — the string
handed to every MCP client on connect — plus "62 (59 framework + 3 meta)" from a tool, "Full
assessment with 59 tools" in a paid-tier upsell, and the same figure in the published
.well-known server card. tools/list returns 6.

The 59 were never imported. The code says so itself, in the comment above list_all_tools:
"In production, these would import from the individual server modules." They live in the
standalone component MCPs. The claim described a product that was never assembled here.

These tests derive every number from the registry, so a count can only be wrong if the registry
is wrong.
"""

from __future__ import annotations

import asyncio
import json
import pathlib
import re

import pytest

import server

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _tools():
    return asyncio.get_event_loop().run_until_complete(server.mcp.list_tools())


@pytest.fixture(scope="module")
def tool_names():
    return [t.name for t in asyncio.run(server.mcp.list_tools())]


def test_derived_count_equals_tools_list(tool_names):
    assert server._registered_tool_names() == sorted(tool_names)


def test_instructions_claim_no_number_the_registry_cannot_back(tool_names):
    instr = server.mcp.instructions or ""
    claimed = [int(n) for n in re.findall(r"\b(\d+)\s+(?:compliance\s+|meta-)?tools?\b", instr)]
    for n in claimed:
        assert n == len(tool_names), (
            f"instructions advertise {n} tools; tools/list serves {len(tool_names)}"
        )


def test_no_stale_59_or_62_anywhere_in_the_served_surface(tool_names):
    # These were the two advertised figures. Neither may reappear as a tool count in anything
    # a client reads: the instructions, the server card, or a tool's own docstring.
    surfaces = {
        "instructions": server.mcp.instructions or "",
        "server-card": (ROOT / ".well-known/mcp/server-card.json").read_text(),
    }
    for t in asyncio.run(server.mcp.list_tools()):
        surfaces[f"tool:{t.name}"] = t.description or ""
    bad = re.compile(r"\b(59|62)\s+(?:compliance\s+|governance\s+|framework\s+)?tools?\b", re.I)
    for where, text in surfaces.items():
        hit = bad.search(text)
        assert not hit, f"{where} still advertises '{hit.group(0)}' against {len(tool_names)} real tools"


def test_server_card_description_matches_the_registry():
    card = json.loads((ROOT / ".well-known/mcp/server-card.json").read_text())
    claimed = [int(n) for n in re.findall(r"\b(\d+)\s+(?:compliance\s+|meta-)?tools?\b", card["description"])]
    n = len(asyncio.run(server.mcp.list_tools()))
    for c in claimed:
        assert c == n, f"server card advertises {c} tools; the server serves {n}"


def test_the_pin_that_keeps_this_importable_is_present():
    # mcp 2.x renamed FastMCP -> MCPServer, so an unbounded ">=1.0.0" resolves to a release this
    # v1 code cannot import at all. Verified: mcp>=1.0.0 resolves 2.1.1 and raises
    # ModuleNotFoundError: No module named 'mcp.server.fastmcp'.
    pyproject = (ROOT / "pyproject.toml").read_text()
    assert "mcp>=1.0.0,<2" in pyproject, "the mcp dependency must stay bounded below 2.x"
