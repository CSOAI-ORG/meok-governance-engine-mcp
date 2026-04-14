# MEOK Governance Engine MCP

**62 AI governance tools in one MCP server.** The most comprehensive compliance MCP in existence.

## Why This MCP Exists

Every organization needs AI governance. Most are struggling with:
- Multiple frameworks (EU AI Act, NIST, ISO 42001, GDPR, SOC 2)
- Complex crosswalk mappings between frameworks
- Expensive consultants for compliance audits
- No way to verify AI system compliance in real-time

**MEOK solves all of this.**

## Features

### Framework Compliance (20+ tools)
- ✅ **EU AI Act** — Risk classification, prohibited practices, high-risk requirements
- ✅ **NIST AI RMF** — GOVERN, MAP, MEASURE, MANAGE functions
- ✅ **ISO 42001** — AI management system certification
- ✅ **GDPR** — Data protection, subject rights, DPO requirements
- ✅ **SOC 2** — Security, availability, confidentiality
- ✅ **ISO 27001** — Information security

### Crosswalk Mapping (12 tools)
- Map between ANY two frameworks via CSOAI
- Find compliance gaps across frameworks
- Generate unified crosswalk reports

### Self-Audit (10 tools)
- Real-time compliance scoring
- Automated audit report generation
- Timestamp compliance certificates
- Full audit trail with evidence

### Governance (12 tools)
- Framework applicability by industry/jurisdiction
- Cost estimation across frameworks
- Penalty risk assessment

## Tools

| Tool | Description |
|------|-------------|
| `full_governance_report` | Comprehensive report for your organization |
| `which_frameworks_apply` | Determine applicable frameworks |
| `compliance_cost_estimator` | Annual compliance cost projection |
| `compliance_score_engine` | Real-time scoring for AI systems |
| `check_compliance` | Framework-specific compliance check |
| `generate_documentation` | Auto-generate compliance docs |
| `assess_penalties` | Calculate potential regulatory penalties |
| `get_timeline` | Regulatory deadline tracker |
| `audit_report` | Formal audit report generator |
| `bridge_frameworks` | Map between two specific frameworks |
| `find_gaps` | Identify missing controls |
| `get_unified_crosswalk` | All 12 frameworks mapped together |

## Quick Start

```bash
pip install meok-governance-engine-mcp
python -m meok_governance_engine_mcp
```

## Example Usage

```python
# Check which frameworks apply
result = which_frameworks_apply(
    industry="healthcare",
    jurisdiction="eu",
    company_size="enterprise"
)

# Calculate compliance score
result = compliance_score_engine(
    system_description="AI-powered diagnostic tool for radiology",
    frameworks="eu_ai_act,nist,iso_42001"
)

# Generate audit report
result = audit_report(
    organization_name="MedTech Corp",
    frameworks=["eu_ai_act", "gdpr"]
)
```

## Competition

| Feature | MEOK | Competitors |
|---------|------|-------------|
| Framework count | 12+ | 1-3 |
| Crosswalk mapping | ✅ | ❌ |
| Self-audit | ✅ | ❌ |
| Real-time scoring | ✅ | ❌ |
| Price | £999/mo | £2k-10k/mo |

## Contact

- **Website**: https://meok.ai
- **Email**: nick@meok.ai
- **Documentation**: https://meok.ai/docs

## License

MIT - MEOK AI Labs
