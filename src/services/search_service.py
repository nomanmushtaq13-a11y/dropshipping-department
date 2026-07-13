from src.database.product_repository import all_products

def by_name(keyword):

    keyword = keyword.lower()

    return [
        p for p in all_products()
        if keyword in p.get("product_name","").lower()
    ]
