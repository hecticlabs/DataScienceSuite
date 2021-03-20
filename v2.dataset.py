import json

out = open('v2.dataset.json', 'w')
inp = open('raw_dataset.txt', 'r')
indat = inp.read().split(' ')
idx = 0
inp.close()

data = {}

while True:
    if idx+1 >= len(indat):
        break
    val = indat[idx]
    val2 = indat[idx+1]
    idx+=1

    if val in data:
        data[val].append(val2)
    else:
        data[val] = [val2]

out.write(json.dumps(data))
out.close()