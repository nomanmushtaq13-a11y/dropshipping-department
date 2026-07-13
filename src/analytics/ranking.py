from src.database.product_repository import all_products

def ranking():

    products=all_products()

    ranked=sorted(
        products,
        key=lambda x: float(x.get("profit_margin",0)),
        reverse=True
    )

    for p in ranked:
        print(
            p.get("product_name"),
            "-",
            p.get("profit_margin"),
            "%"
        )
