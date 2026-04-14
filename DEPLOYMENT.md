# MEOK Governance Engine — Deployment Guide

## Option 1: Standalone (Recommended for evaluation)
The Governance Engine runs as a SINGLE MCP server with 62 tools built-in.
No sub-servers needed. Install and run:
```bash
pip install mcp
python server.py
```

## Option 2: Pack Installation (Full framework access)
For deeper per-framework tools, install individual servers:
```bash
git clone https://github.com/CSOAI-ORG/eu-ai-act-compliance-mcp
git clone https://github.com/CSOAI-ORG/nist-rmf-ai-mcp
git clone https://github.com/CSOAI-ORG/iso-42001-ai-mcp
# ... etc
```

## Option 3: Enterprise (Managed deployment)
Contact nicholas@meok.ai for:
- Dedicated deployment on your infrastructure
- Air-gapped mode for defense/regulated environments
- Custom framework configurations
- SLA and support

## Claude Desktop Configuration
```json
{
  "mcpServers": {
    "meok-governance": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/path/to/meok-governance-engine-mcp"
    }
  }
}
```

## Pricing
- Free: 5 calls/day (evaluation)
- Pro: £299/mo (single framework)
- Business: £999/mo (all frameworks)
- Enterprise: £2,500/mo (custom + SLA)
