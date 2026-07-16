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
        self.write(rows,data.keys())

    def write(self,rows,headers=None):

        os.makedirs(os.path.dirname(self.path),exist_ok=True)

        if headers is None:
            if rows:
                headers=rows[0].keys()
            else:
                headers=[]

        with open(self.path,"w",newline='',encoding='utf-8') as f:

            if headers:
                writer=csv.DictWriter(f,fieldnames=headers)
                writer.writeheader()

                if rows:
                    writer.writerows(rows)

    def find(self,key,value):

        for row in self.read():

            if row.get(key)==str(value):
                return row

        return None

    def update(self,key,value,new_data):

        rows=self.read()

        for row in rows:

            if row.get(key)==str(value):
                row.update(new_data)

        self.write(rows)

    def delete(self,key,value):

        rows=[r for r in self.read() if r.get(key)!=str(value)]

        headers=rows[0].keys() if rows else ["id"]

        self.write(rows,headers)

    def count(self):
        return len(self.read())
