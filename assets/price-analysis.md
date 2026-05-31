# Price Analysis Template

Use this structure when presenting pricing analysis results.

---

## 💲 {product_name} — Price Analysis

**SKU:** {sku} | **Category:** {category} | **Date:** {analysis_date}

### Current Pricing

| Field | Value |
|-------|-------|
| List Price | ${list_price} |
| Cost | ${unit_cost} |
| Margin | {margin_pct}% |
| MAP | ${map_price} |

### Competitive Landscape

| Competitor | Price | Difference |
|-----------|-------|-----------|
| {competitor_name} | ${competitor_price} | {diff_emoji} {diff_pct}% |

{diff_emoji mapping: lower=🔻, higher=🔺, similar=➡️}

### Price Recommendation

| Scenario | Price | Margin | Expected Volume |
|----------|-------|--------|----------------|
| Aggressive | ${aggressive_price} | {agg_margin}% | {agg_volume} |
| Optimal | ${optimal_price} | {opt_margin}% | {opt_volume} |
| Premium | ${premium_price} | {prem_margin}% | {prem_volume} |

**Recommended:** ${recommended_price} ({recommendation_rationale})

{if margin_pct < 15: "⚠️ Thin margin — review cost structure before discounting"}
{if diff_pct > 20: "🚨 Significantly above market — risk of volume loss"}
{if diff_pct < -20: "⚠️ Well below market — margin opportunity exists"}

---

*Generated from mcp-pricing | {timestamp}*
