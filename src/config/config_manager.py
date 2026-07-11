import json

class Config:

    def __init__(self,path="config/settings.json"):

        with open(path,"r") as f:
            self.data=json.load(f)

    def get(self,key):

        return self.data.get(key)

config=Config()
