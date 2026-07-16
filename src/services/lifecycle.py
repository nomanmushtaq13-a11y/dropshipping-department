from src.database.product_repository import update_product

def move(product_id,status):

    update_product(
        product_id,
        {
            "status":status
        }
    )

    print(
        "Product moved to:",
        status
    )
