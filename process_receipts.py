import os
import glob
import json
import shutil
import fnmatch

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")
#file = "C:/Users/seeni/Desktop/python-projects/receipts/new"
#receipts  = fnmatch.fnmatch(''.', "*['0-9'].json")

subtotal = 0.0
#print(receipts)

for path in glob.iglob("./new/receipts-*[0-9].json"):
    
    try:
        with open(path) as f:
            content = json.load(f)
            subtotal += float(content['value'])
        #name = path.split("\\")[-1]
           # print(name)
        
        destination = path.replace('new', 'processed')
        shutil.move(path, destination)
        print(f"moved '{path}' to '{destination}'")
        
    except OSError as err:
            print(err)


#import math
print(f"Receipt subtotal: ${round(subtotal, 2)}")
#print(f"Receipt subtotal: ${math.floor(subtotal)}")
