n_blocks = int(input())
d = {}

for _ in range(n_blocks):
    w, h = map(int, input().split())
    if w not in d:
        d[w] = h
    else:
        d[w] = max(d[w], h)

print(sum(d.values()))
