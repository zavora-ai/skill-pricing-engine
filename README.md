# Pricing Engine Skill

> Dynamic pricing for AI agents — CEL rule waterfalls, promotions (BOGO/volume/flash), customer segments, quotes, 170+ currency conversion, and 50+ country tax calculation.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--pricing-green)](https://github.com/zavora-ai/mcp-pricing)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | What It Achieves |
|----------|-------|------------------|
| Calculate Price | 1 | Full waterfall with explanation |
| Create & Activate Rule | 3 | Create → test → activate safely |
| Run Promotion | 2 | BOGO, volume, flash, coupon |
| Generate Quote | 2 | Lock prices for customer |
| Multi-Currency | 2 | Price + FX conversion |

### Without This Skill vs With

| Without | With |
|---------|------|
| Static price lists | Dynamic CEL-based rules |
| Manual discounts | Automated segment pricing |
| No margin protection | Floor/ceiling guards |
| Spreadsheet quotes | Locked, versioned quotes |
| Single currency | 170+ currencies live |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-pricing-engine.git \
  ~/.skills/skills/pricing-engine
```

## Requirements

**Required:** `mcp-pricing` (26 tools)

**Cross-MCP:**
- `mcp-pos` — dynamic checkout pricing
- `mcp-crm` — segment-based pricing
- `mcp-sales` — quote pipeline
- `mcp-inventory` — clearance pricing for overstock

## Folder Structure

```
pricing-engine/
├── SKILL.md                       # Decision tree + CEL examples + margin protection
├── scripts/
│   └── margin_check.py            # Verify price maintains minimum margin
├── references/
│   ├── tool-sequences.md          # 26 tools + action types
│   ├── cross-mcp-workflows.md     # Pricing + POS + CRM + Sales + Inventory
│   └── examples.md                # Waterfall, Black Friday rule, quote
├── README.md
└── LICENSE
```

## Example

**User:** "Create a 25% off rule for electronics on Black Friday"

**Result:**
```
Rule created: "Black Friday Electronics"
Condition: catalog.category == "electronics"
Action: 25% discount
Tested: ✅ pass
Scheduled: Nov 29, 00:00–23:59 UTC
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Margin protection | Floor never breached |
| Rule safety | Always tested before activation |
| Audit trail | Every price change logged |
| Conflict detection | No overlapping rules at same priority |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
