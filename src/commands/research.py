from src.services.research_queue import create

def run():

    product=input("Product: ")
    category=input("Category: ")
    country=input("Country: ")
    source=input("Source: ")

    create(product,category,country,source)
