from src.database.product_repository import all_products
from src.services.approval import approve

def run():

    products=all_products()

    for product in products:

        status=approve(product)

        print(
            product["product_name"],
            "=>",
            status
        )
