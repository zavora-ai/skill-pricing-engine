# Pricing Cross-MCP Workflows

## Pricing + POS: Dynamic Checkout
```
PRICING: price_calculate(sku, customer_id, channel: "retail") → final price
POS: cart_add_item(cart_id, sku, price: calculated)
```

## Pricing + CRM: Segment Pricing
```
CRM: get_contact(id) → {segment: "enterprise"}
PRICING: price_calculate(sku, customer_id) → segment discount applied
```

## Pricing + Sales: Quote Pipeline
```
SALES: get_opportunity(id) → items needed
PRICING: quotes_create(customer, items, valid_days: 30)
SALES: update_opportunity(id, quote_id)
```

## Pricing + Inventory: Clearance Pricing
```
INVENTORY: stock_check(sku) → {available: 5, reorder_point: 50}
→ Overstocked? Create clearance rule
PRICING: rules_create(name: "Clearance", condition: 'item.sku == "OLD-001"', actions: [{type: "pct_discount", value: 40}])
```
