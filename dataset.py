import json

out = open('dataset.json', 'w')
inp = open('raw_dataset.txt', 'r')

data = {}

while True:
    val = inp.read(1)
    tell = inp.tell()
    val2 = inp.read(1)
    val3 = inp.read(1)
    val4 = inp.read(1)
    val5 = inp.read(1)
    if bytes(val, 'utf-8') == b'' or  bytes(val2, 'utf-8') == b'' or  bytes(val3, 'utf-8') == b'' or  bytes(val4, 'utf-8') == b'':
        break
    inp.seek(tell)

    key = val + val2 + val3 + val4

    if key in data:
        data[key].append(val5)
    else:
        data[key] = [val5]

inp.close()
out.write(json.dumps(data))
out.close()