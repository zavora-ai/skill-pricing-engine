---
name: pricing-engine
description: Orchestrate pricing operations — calculate prices through waterfall rules, create/manage CEL-based pricing rules, run promotions (BOGO, volume tiers, flash sales), manage customer segments, generate quotes, convert currencies, and calculate taxes. Use when calculating prices, creating discount rules, running promotions, quoting customers, converting currencies, or computing taxes.
version: "1.0.0"
license: Apache-2.0
compatibility: Requires mcp-pricing server connected. CEL expression engine, 170+ currencies, 50+ country tax rates.
allowed-tools:
  - price_calculate
  - rules_create
  - rules_list
  - rules_activate
  - rules_deactivate
  - rules_update
  - rules_history
  - rules_schedule
  - rules_conflicts
  - rules_test
  - rules_validate
  - catalog_upsert
  - catalog_get
  - catalog_list
  - segments_create
  - segments_list
  - promotions_create
  - promotions_list
  - promotions_apply
  - quotes_create
  - quotes_get
  - quotes_approve
  - market_fx_convert
  - market_fx_rates
  - market_tax
  - audit_log
tags:
  - business
  - pricing
  - revenue
  - promotions
  - quotes
  - fx
  - tax
references:
  - references/tool-sequences.md
  - references/cross-mcp-workflows.md
  - references/examples.md
metadata:
  author: Zavora AI
  mcp-server: mcp-pricing
  category: mcp-enhancement
  success-criteria:
    trigger-rate: "95% on pricing queries"
    margin-protection: "Floor price never breached"
    rule-safety: "Always test rules before activating"
    audit: "Every price change logged"
---

# Pricing Engine

You manage pricing strategy — calculate prices through rule waterfalls, create dynamic pricing rules with CEL conditions, run promotions, generate quotes, and handle multi-currency + tax. Always test rules before activating. Never breach floor prices.

## Decision Tree

```
├── "price", "how much", "calculate"? → price_calculate (explain=true)
├── "rule", "discount rule", "pricing logic"? → rules_create / rules_list
├── "activate", "turn on rule"? → rules_activate
├── "schedule", "start at midnight"? → rules_schedule
├── "promotion", "coupon", "BOGO", "flash sale"? → promotions_create / promotions_apply
├── "segment", "gold tier", "enterprise"? → segments_create / segments_list
├── "quote", "proposal", "lock price"? → quotes_create / quotes_approve
├── "convert", "USD to KES", "FX"? → market_fx_convert
├── "tax", "VAT", "GST"? → market_tax
├── "conflict", "overlapping rules"? → rules_conflicts
├── "test rule", "dry run"? → rules_test
├── "history", "who changed"? → rules_history / audit_log
```

## Key Workflows

### Calculate Price (1 call)
`price_calculate(sku, customer_id, quantity, channel, explain: true)` → final price with waterfall breakdown

### Create & Activate Rule (3 calls)
1. `rules_create(name, condition_cel, actions, priority)` → rule_id
2. `rules_test(rule_id, test_cases)` → all pass ✅
3. `rules_activate(rule_id)` → live

### Run Promotion (2 calls)
1. `promotions_create(type: "bogo", sku, start, end)` → promo_id
2. `promotions_apply(promo_code, sku, quantity)` → discounted price

### Generate Quote (2 calls)
1. `quotes_create(customer_id, items, valid_days: 30)` → quote with locked prices
2. `quotes_approve(quote_id)` → approved, prices locked

### Multi-Currency Price (2 calls)
1. `price_calculate(sku, customer_id)` → price in base currency
2. `market_fx_convert(amount, from: "KES", to: "USD")` → converted

## MUST DO
- Always `rules_test` before `rules_activate` (never go live untested)
- Check `rules_conflicts` when creating rules at same priority
- Use `explain: true` on `price_calculate` to show waterfall
- Set floor prices to protect margins
- Log all overrides via `audit_log`

## MUST NOT DO
- Don't activate rules without testing first
- Don't create rules without floor/ceiling guards
- Don't approve quotes without checking margin
- Don't ignore rule conflicts (same priority = unpredictable)

## Cross-MCP Orchestration

### Pricing + POS: Dynamic Checkout
```
PRICING: price_calculate(sku: "WIDGET-001", customer_id: "C-100", channel: "retail")
  → {final: 450, breakdown: [{rule: "Gold tier -10%", applied: -50}]}
POS: cart_add_item(cart_id, sku: "WIDGET-001", price: 450)
```

### Pricing + CRM: Segment-Based Pricing
```
CRM: get_contact(id) → {segment: "enterprise", annual_spend: 500000}
PRICING: price_calculate(sku, customer_id, explain: true)
  → Enterprise discount applied automatically via segment rule
```

### Pricing + Sales: Quote Generation
```
SALES: get_opportunity(id) → {customer: "Acme", items: [...]}
PRICING: quotes_create(customer: "Acme", items, valid_days: 30)
  → Locked prices for 30 days
SALES: update_opportunity(id, quote_id)
```

## CEL Expression Examples

```cel
// Gold customers get 10% off
customer.segment == "gold"

// Volume discount: 100+ units
item.quantity >= 100

// Channel-specific: marketplace markup
item.channel == "marketplace"

// High-value customer
customer.annual_spend > 1000000

// Category + quantity combo
catalog.category == "electronics" && item.quantity >= 5
```

## Troubleshooting

**CONDITION_PARSE_ERROR:** CEL syntax wrong. Use `rules_validate` to check before saving.

**Rule not applying:** Check priority order. Higher priority rules execute first. Check if rule is activated.

**Floor breached:** Multiple discounts stacking. Add `set_floor` action to protect margin.
