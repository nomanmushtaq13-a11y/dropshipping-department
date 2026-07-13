import csv

DB="database/products/master.csv"

def delete(product_id):
    rows=[]

    with open(DB,newline='',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        headers=reader.fieldnames

        for row in reader:
            if row["id"]!=str(product_id):
                rows.append(row)

    with open(DB,'w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print("Deleted Successfully")
