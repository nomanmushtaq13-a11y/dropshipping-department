import shutil
import os

def export():

    os.makedirs("exports",exist_ok=True)

    shutil.copy(
        "database/products/master.csv",
        "exports/products_export.csv"
    )

    print("Export Complete")
