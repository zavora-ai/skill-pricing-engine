# Pricing Examples

## Example 1: "What's the price for SKU WIDGET-001 for our gold customer?"
```
price_calculate(sku: "WIDGET-001", customer_id: "C-100", explain: true)
→ {
    final_price: 450,
    waterfall: [
      {step: "List price", value: 500},
      {step: "Gold tier rule (-10%)", value: -50},
      {step: "Floor check (min 400)", value: "pass"}
    ]
  }
```
Response: "WIDGET-001 for Gold customer: KES 450 (list 500, Gold -10% = -50). Floor: 400 ✅"

## Example 2: "Create a Black Friday rule — 25% off electronics"
```
rules_create(
  name: "Black Friday Electronics",
  condition: 'catalog.category == "electronics"',
  actions: [{type: "pct_discount", value: 25}],
  priority: 10
) → {rule_id: "RULE-042"}
rules_test(rule_id: "RULE-042", cases: [{sku: "LAPTOP-001", expected_discount: 25}]) → pass ✅
rules_schedule(rule_id: "RULE-042", activate_at: "2026-11-29T00:00:00Z", deactivate_at: "2026-11-29T23:59:59Z")
```
Response: "Black Friday rule created and scheduled. 25% off electronics, Nov 29 only. Tested ✅"

## Example 3: "Generate a quote for Acme Corp — 50 widgets at volume pricing"
```
price_calculate(sku: "WIDGET-001", customer_id: "ACME", quantity: 50, explain: true)
→ {final: 425, rule: "Volume 50+ = -15%"}
quotes_create(customer: "ACME", items: [{sku: "WIDGET-001", qty: 50, price: 425}], valid_days: 30)
→ {quote_id: "QT-2026-089", total: 21250, expires: "2026-06-27"}
```
Response: "Quote QT-2026-089: 50× WIDGET-001 @ KES 425 = KES 21,250. Valid 30 days. Pending approval."
