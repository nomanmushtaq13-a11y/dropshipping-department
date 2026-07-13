from src.services.search_service import by_name

def run():

    keyword=input("Search: ")

    results=by_name(keyword)

    print()

    for r in results:

        print(r)
