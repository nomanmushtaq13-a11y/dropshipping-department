import csv
import os

class CSVDatabase:

    def __init__(self, path):
        self.path = path

    def exists(self):
        return os.path.exists(self.path)

    def read(self):
        if not self.exists():
            return []

        with open(self.path,newline='',encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def append(self,data):

        file_exists=self.exists()

        with open(self.path,'a',newline='',encoding='utf-8') as f:

            writer=csv.DictWriter(f,fieldnames=data.keys())

            if not file_exists:
                writer.writeheader()

            writer.writerow(data)
