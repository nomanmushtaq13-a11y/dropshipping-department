from src.database.supplier_repository import all_suppliers

def run():

    suppliers=all_suppliers()

    print("="*50)
    print("SUPPLIERS")
    print("="*50)

    for s in suppliers:

        print(s)
