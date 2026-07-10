import csv
import os

DB_FILE = "database/products/master.csv"

HEADERS = [
    "id",
    "product_name",
    "category",
    "target_country",
    "cost_usd",
    "selling_price_usd",
    "profit_margin",
    "demand_score",
    "competition_score",
    "organic_score",
    "supplier",
    "status"
]

def ensure_database():
    if not os.path.exists(DB_FILE):
        os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
        with open(DB_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)

def add_product():
    ensure_database()

    with open(DB_FILE, "r", newline="") as f:
        rows = list(csv.reader(f))

    product_id = len(rows)

    name = input("Product Name: ")
    category = input("Category: ")
    country = input("Target Country: ")
    cost = input("Cost USD: ")
    sell = input("Selling Price USD: ")
    margin = input("Profit Margin %: ")
    demand = input("Demand Score (0-10): ")
    competition = input("Competition Score (0-10): ")
    organic = input("Organic Score (0-10): ")
    supplier = input("Supplier: ")

    with open(DB_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            product_id,
            name,
            category,
            country,
            cost,
            sell,
            margin,
            demand,
            competition,
            organic,
            supplier,
            "Pending"
        ])

    print("\n✅ Product added successfully!")

if __name__ == "__main__":
    add_product()
