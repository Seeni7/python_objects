import random
import json
import os

directory = "new"
parent_dir = "C:/Users/seeni/Desktop/python-projects/receipts"
count = int(os.getenv("FILE_COUNT") or 10)
words = [word.strip() for word in open('words.txt')]
path = os.path.join(parent_dir, directory)
try:
    os.mkdir(path)
except OSError:
    print("folder new already exists")

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open(f'./new/receipts-{identifier}.json', 'w') as f:
        json.dump(content, f)
