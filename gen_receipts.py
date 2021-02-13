import random
import json
import os

directory = "new"
parent_dir = "C:/Users/seeni/Desktop/python-projects/receipts"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
count = int(os.getenv("FILE_COUNT") or 10)
words = [word.strip() for word in open('words.txt').readline()]


for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open(f'./new/receipts-{identifier}.json', 'w') as f:
        json.dump(content, f)
