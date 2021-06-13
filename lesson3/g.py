n = int(input())

pairs = set()
for _ in range(n):
    a, b = map(int, input().split())
    pairs.add((a, b))

cnt = 0
for pair in pairs:
    a, b = pair
    if a + b + 1 == n and b >= 0 and a >= 0:
        cnt += 1

print(cnt)
