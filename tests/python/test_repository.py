from src.database.product_repository import all_products

products = all_products()

print("Products in database:", len(products))
