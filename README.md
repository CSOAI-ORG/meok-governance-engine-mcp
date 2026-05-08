<div align="center">

# Meok Governance Engine MCP

**MCP server for meok governance engine mcp operations**

[![PyPI](https://img.shields.io/pypi/v/meok-governance-engine-mcp)](https://pypi.org/project/meok-governance-engine-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-MCP_Server-purple)](https://meok.ai)

</div>

## Overview

Meok Governance Engine MCP provides AI-powered tools via the Model Context Protocol (MCP).

## Tools

| Tool | Description |
|------|-------------|
| `full_governance_report` | Generate a COMPLETE multi-framework governance report in one call. |
| `which_frameworks_apply` | Instantly determine which AI governance frameworks apply to your situation. |
| `compliance_cost_estimator` | Estimate compliance costs and show how MEOK Governance Engine saves money. |
| `list_all_tools` | List all 62 governance tools available in this engine. |
| `compliance_score_engine` | Calculate compliance percentage per framework. Input system description, get sco |
| `get_full_audit_trail` | Get timestamped audit trail of all governance checks performed. |

## Installation

```bash
pip install meok-governance-engine-mcp
```

## Usage with Claude Desktop

Add to your Claude Desktop MCP config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "meok-governance-engine-mcp": {
      "command": "python",
      "args": ["-m", "meok_governance_engine_mcp.server"]
    }
  }
}
```

## Usage with FastMCP

```python
from mcp.server.fastmcp import FastMCP

# This server exposes 6 tool(s) via MCP
# See server.py for full implementation
```

## License

MIT © [MEOK AI Labs](https://meok.ai)
