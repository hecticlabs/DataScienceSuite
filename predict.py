import json, random

dataset = None
with open('dataset.json', 'r') as inp:
    dataset = json.loads(inp.read())

text = input("Write a starting point: ")
steps = 0
while steps < 2000:
    key = text[-4] + text[-3] + text[-2] + text[-1]
    if key in dataset:
        text += random.choice(dataset[key])
    else:
        break
    steps += 1
print(text)