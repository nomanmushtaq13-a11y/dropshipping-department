from src.database.csv_engine import CSVDatabase
from src.config.settings import settings

db=CSVDatabase(settings.SUPPLIER_DB)

def add_supplier(data):

    db.append(data)

def all_suppliers():

    return db.read()
