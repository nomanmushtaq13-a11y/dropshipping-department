from src.database.csv_engine import CSVDatabase

db = CSVDatabase("database/research/queue.csv")

def add(data):
    db.append(data)

def all():
    return db.read()
