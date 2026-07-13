import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME=os.getenv("APP_NAME")
APP_VERSION=os.getenv("APP_VERSION")

PRODUCT_DB=os.getenv("PRODUCT_DB")
SUPPLIER_DB=os.getenv("SUPPLIER_DB")
