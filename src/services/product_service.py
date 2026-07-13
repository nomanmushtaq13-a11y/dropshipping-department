from src.database.product_repository import add_product
from src.validators.product_validator import validate

def create(product):

    ok,message = validate(product)

    if not ok:
        raise ValueError(message)

    add_product(product)

    return message
