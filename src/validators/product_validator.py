def validate(product):
    required = [
        "product_name",
        "category",
        "cost_usd",
        "selling_price_usd"
    ]

    missing = [k for k in required if not product.get(k)]

    if missing:
        return False, f"Missing fields: {', '.join(missing)}"

    return True, "OK"
