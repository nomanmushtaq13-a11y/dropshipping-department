from src.database.csv_engine import CSVDatabase
from src.config.settings import settings

db = CSVDatabase(settings.PRODUCT_DB)

def add_product(product):

    db.append(product)

def all_products():

    return db.read()
