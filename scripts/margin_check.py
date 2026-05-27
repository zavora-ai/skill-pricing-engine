#!/usr/bin/env python3
"""Check if price maintains minimum margin above cost."""
import json, sys

def check(data):
    price = data["price"]
    cost = data["cost"]
    min_margin_pct = data.get("min_margin_pct", 20)
    margin = ((price - cost) / price) * 100 if price > 0 else 0
    return {
        "price": price,
        "cost": cost,
        "margin_pct": round(margin, 1),
        "min_required": min_margin_pct,
        "safe": margin >= min_margin_pct,
        "action": "OK" if margin >= min_margin_pct else f"Price too low — margin {margin:.1f}% < {min_margin_pct}%"
    }

if __name__ == "__main__":
    print(json.dumps(check(json.loads(sys.argv[1])), indent=2))
