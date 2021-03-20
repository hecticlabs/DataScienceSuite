import json, random, sys

dataset = None
with open('v2.dataset.json', 'r') as inp:
    dataset = json.loads(inp.read())

if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    text = input("Write a starting point: ")
if not text.endswith(' '): text += ' '

steps = 0
while steps < 5000:
    key = text.split(' ')[-2]
    if key in dataset:
        text += random.choice(dataset[key]) + ' '
    else:
        break
    steps += 1
print(text)