from src.database.product_repository import all_products

def summary():
    products=all_products()

    print("="*40)
    print("PRODUCT SUMMARY")
    print("="*40)

    print("Total Products:",len(products))

    approved=0

    for p in products:
        if p.get("status")=="Approved":
            approved+=1

    print("Approved:",approved)
    print("Pending:",len(products)-approved)
