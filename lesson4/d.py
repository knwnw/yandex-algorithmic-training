n_keys = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))

d = {i + 1: value for i, value in enumerate(c)}

for key in p:
    d[key] -= 1

for key in d:
    print('YES' if d[key] < 0 else 'NO')
