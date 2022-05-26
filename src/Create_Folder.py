import os
from datetime import datetime

now = datetime.now()

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)
    except OSError:
        print('Error : Creating Directory '+directory)
