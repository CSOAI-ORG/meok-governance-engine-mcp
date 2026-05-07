[![meok-governance-engine-mcp MCP server](https://glama.ai/mcp/servers/CSOAI-ORG/meok-governance-engine-mcp/badges/score.svg)](https://glama.ai/mcp/servers/CSOAI-ORG/meok-governance-engine-mcp)
[![MCP Registry](https://img.shields.io/badge/MCP_Registry-Published-green)](https://registry.modelcontextprotocol.io)
[![PyPI](https://img.shields.io/pypi/v/meok-governance-engine-mcp)](https://pypi.org/project/meok-governance-engine-mcp/)

[![meok-governance-engine-mcp MCP server](https://glama.ai/mcp/servers/CSOAI-ORG/meok-governance-engine-mcp/badges/card.svg)](https://glama.ai/mcp/servers/CSOAI-ORG/meok-governance-engine-mcp)

<div align="center">

[![PyPI](https://img.shields.io/pypi/v/meok-governance-engine-mcp)](https://pypi.org/project/meok-governance-engine-mcp/)
[![Downloads](https://img.shields.io/pypi/dm/meok-governance-engine-mcp)](https://pypi.org/project/meok-governance-engine-mcp/)
[![GitHub stars](https://img.shields.io/github/stars/CSOAI-ORG/meok-governance-engine-mcp)](https://github.com/CSOAI-ORG/meok-governance-engine-mcp/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

# Governance Engine MCP

**62 AI governance tools across 13 regulatory frameworks in one MCP server.**

EU AI Act · DORA · NIS2 · CRA · GDPR · CSRD · HIPAA · SOC 2 · ISO 42001 · ISO 27001 · NIST AI RMF · PCI DSS · UK AI Bill

[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-224+_servers-purple)](https://meok.ai)

[Install](#install) · [Tools](#tools) · [Pricing](#pricing) · [Attestation API](#attestation-api)

</div>

---

## Why This Exists

Most compliance teams run separate audits for each regulation. A fintech deploying AI needs DORA + EU AI Act + NIS2 + GDPR simultaneously. Running four separate tools means four skill sets, four invoices, and four months of consultant time.

This MCP orchestrates all 13 frameworks from a single Claude prompt. One audit covers every regulation your product touches. Each finding gets an HMAC-signed attestation your auditor can verify independently.

## Install

```bash
pip install meok-governance-engine-mcp
```

## Tools

| Tool | Framework | What it does |
|------|-----------|-------------|
| `run_unified_audit` | All 13 | Cross-framework compliance sweep |
| `classify_risk_eu_ai_act` | EU AI Act | Article 6 risk tier classification |
| `assess_dora_resilience` | DORA | 5-pillar ICT resilience assessment |
| `check_nis2_obligations` | NIS2 | Essential/important entity obligations |
| `evaluate_cra_requirements` | CRA | Annex IV security requirements |
| `run_gdpr_dpia` | GDPR | Data protection impact assessment |
| `check_hipaa_safeguards` | HIPAA | Administrative/technical/physical safeguards |
| `assess_soc2_controls` | SOC 2 | Trust Service Criteria evaluation |
| `check_iso42001` | ISO 42001 | AI management system assessment |
| `generate_ai_bom` | NIST/CycloneDX | AI bill of materials |
| `sign_audit_receipt` | All | HMAC-SHA256 signed attestation |

## Example

```
Prompt: "Run a unified governance audit on our customer-facing chatbot.
It processes EU personal data, is deployed by a German bank,
and uses GPT-4 as the backbone model."

Result: Cross-framework report covering EU AI Act (high-risk, Annex III),
DORA (ICT third-party risk), NIS2 (essential entity), GDPR (DPIA required),
CRA (default security settings). Each finding signed with attestation cert.
```

## Pricing

| Tier | Price | What you get |
|------|-------|-------------|
| **Free** | £0 | 10 calls/day — unified audit + risk classification |
| **Pro** | £199/mo | Unlimited + HMAC-signed attestations + verify URLs |
| **Enterprise** | £1,499/mo | Multi-tenant + co-branded reports + webhooks |

[Subscribe to Pro](https://buy.stripe.com/14A4gB3K4eUWgYR56o8k836) · [Enterprise](https://buy.stripe.com/4gM9AV80kaEG0ZT42k8k837)

## Attestation API

Every Pro/Enterprise audit produces a cryptographically signed certificate:

```
POST https://meok-attestation-api.vercel.app/sign
GET  https://meok-attestation-api.vercel.app/verify/{cert_id}
```

Zero-dep verifier: `pip install meok-attestation-verify`

## Links

- Website: [meok.ai](https://meok.ai)
- All MCP servers: [meok.ai/labs/mcp/servers](https://meok.ai/labs/mcp/servers)
- Enterprise support: nicholas@csoai.org

## License

MIT
<!-- mcp-name: io.github.CSOAI-ORG/meok-governance-engine-mcp -->
