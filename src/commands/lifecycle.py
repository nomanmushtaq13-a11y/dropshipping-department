from src.services.lifecycle import move

def run():

    product=input("Product ID: ")

    status=input("Status: ")

    move(product,status)
