from src.database.csv_engine import CSVDatabase
from src.config.settings import settings

db=CSVDatabase(settings.PRODUCT_DB)

def add_product(product):
    db.append(product)

def all_products():
    return db.read()

def find_product(product_id):
    return db.find("id",product_id)

def update_product(product_id,data):
    db.update("id",product_id,data)

def delete_product(product_id):
    db.delete("id",product_id)

def total_products():
    return db.count()
