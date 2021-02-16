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
receipts = glob.glob("./new/receipts-*[0-9].json")
#receipts  = fnmatch.fnmatch(''.', "*['0-9'].json")

subtotal = 0.0
#print(receipts)

for path in receipts:
    print(receipts)
    try:
        with open(path) as f:
            content = json.load(f)
            subtotal += float(content['value'])
        name = path.split("\\")[-1]
           # print(name)
        destination = (f"./processed/{name}")
        shutil.move(path, destination)
        print(f"moved '{path}' to '{destination}'")
        
    except OSError as err:
            print(err)


print("Receipt subtotal: $%.2f" % subtotal)

