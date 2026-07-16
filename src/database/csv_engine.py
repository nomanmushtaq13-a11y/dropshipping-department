import csv
import os

class CSVDatabase:

    def __init__(self,path):
        self.path=path

    def exists(self):
        return os.path.exists(self.path)

    def read(self):

        if not self.exists():
            return []

        with open(self.path,newline='',encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def append(self,data):

        rows=self.read()

        rows.append(data)

        self.write(rows)

    def write(self,rows):

        if len(rows)==0:
            return

        os.makedirs(os.path.dirname(self.path),exist_ok=True)

        with open(self.path,"w",newline='',encoding='utf-8') as f:

            writer=csv.DictWriter(f,fieldnames=rows[0].keys())

            writer.writeheader()

            writer.writerows(rows)

    def find(self,key,value):

        for row in self.read():

            if row.get(key)==str(value):

                return row

        return None

    def update(self,key,value,new_data):

        rows=self.read()

        for i,row in enumerate(rows):

            if row.get(key)==str(value):

                rows[i].update(new_data)

        self.write(rows)

    def delete(self,key,value):

        rows=[r for r in self.read() if r.get(key)!=str(value)]

        self.write(rows)

    def count(self):

        return len(self.read())
