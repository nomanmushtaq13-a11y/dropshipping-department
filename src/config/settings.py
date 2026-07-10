import os

class Settings:
    APP_NAME = "Dropshipping Department"
    VERSION = "1.0.0-dev"

    DATABASE_DIR = "database"

    PRODUCT_DB = os.path.join(DATABASE_DIR, "products/master.csv")
    SUPPLIER_DB = os.path.join(DATABASE_DIR, "suppliers/master.csv")
    COMPETITOR_DB = os.path.join(DATABASE_DIR, "competitors/master.csv")

    DEFAULT_COUNTRY = "United States"
    DEFAULT_CURRENCY = "USD"

settings = Settings()
