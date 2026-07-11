from src.database.product_repository import all_products

def run():
    products = all_products()

    print("=" * 50)
    print("PRODUCT DATABASE")
    print("=" * 50)

    if not products:
        print("No products found.")
        return

    for index, product in enumerate(products, start=1):
        print(f"{index}. {product.get('product_name','Unknown')} | {product.get('status','N/A')}")
