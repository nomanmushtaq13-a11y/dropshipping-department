from src.database.research_repository import add

def create(product,category,country,source):

    add({
        "product_name":product,
        "category":category,
        "target_country":country,
        "source":source,
        "status":"Pending"
    })

    print("Research task created.")
