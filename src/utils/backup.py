import shutil
import os
from datetime import datetime

def backup(source):

    os.makedirs("backups",exist_ok=True)

    filename=datetime.now().strftime("%Y%m%d_%H%M%S")+".csv"

    destination=os.path.join("backups",filename)

    shutil.copy(source,destination)

    print("Backup Created:",destination)
