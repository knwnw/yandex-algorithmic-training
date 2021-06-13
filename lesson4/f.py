import sys


data = sys.stdin.read()
d = {}

for line in data.strip().split('\n'):
    name, item, quantity = line.strip().split()
    if name not in d:
        d[name] = {item: int(quantity)}
    else:
        if item not in d[name]:
            d[name][item] = int(quantity)
        else:
            d[name][item] += int(quantity)

for name in sorted(d):
    print(f'{name}:')
    for item in sorted(d[name]):
        print(item, d[name][item])
