from src.database.research_repository import all

def run():

    for row in all():
        print(row)
