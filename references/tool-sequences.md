# Pricing Tool Sequences (26 tools)

## Price Calculation (1)
| Tool | Purpose |
|------|---------|
| `price_calculate` | Full waterfall with CEL rules (explain=true for breakdown) |

## Rules Management (9)
| Tool | Purpose |
|------|---------|
| `rules_create` | Create rule with CEL condition + actions |
| `rules_list` | All rules |
| `rules_activate` | Turn on (affects prices) |
| `rules_deactivate` | Turn off |
| `rules_update` | Edit (versioned) |
| `rules_history` | Version history |
| `rules_schedule` | Time-based activation |
| `rules_conflicts` | Detect overlapping rules |
| `rules_test` | Dry-run against test cases |
| `rules_validate` | Check CEL syntax |

## Catalog (3)
| Tool | Purpose |
|------|---------|
| `catalog_upsert` | Add/update product (SKU, price, cost) |
| `catalog_get` | Get product by SKU |
| `catalog_list` | All products |

## Segments (2)
| Tool | Purpose |
|------|---------|
| `segments_create` | Create segment with CEL condition |
| `segments_list` | All segments |

## Promotions (3)
| Tool | Purpose |
|------|---------|
| `promotions_create` | BOGO, volume tier, flash sale, coupon |
| `promotions_list` | All promotions |
| `promotions_apply` | Apply promo code → discounted price |

## Quotes (3)
| Tool | Purpose |
|------|---------|
| `quotes_create` | Lock prices for customer |
| `quotes_get` | Get quote details |
| `quotes_approve` | Approve (governance gate) |

## Market Data (3)
| Tool | Purpose |
|------|---------|
| `market_fx_convert` | Convert between 170+ currencies |
| `market_fx_rates` | Live FX rates |
| `market_tax` | VAT/GST/sales tax (50+ countries) |

## Audit (1)
| Tool | Purpose |
|------|---------|
| `audit_log` | Immutable price change trail |

## Action Types
| Action | Effect |
|--------|--------|
| `pct_discount` | Reduce by N% |
| `absolute_discount` | Reduce by fixed amount |
| `markup_pct` | Increase by N% |
| `set_price` | Override to fixed |
| `multiply_price` | Surge pricing |
| `set_floor` | Minimum price guard |
| `set_ceiling` | Maximum price guard |
