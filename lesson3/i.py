def make_set(m: int):
    s = set()
    for _ in range(m):
        s.add(input())
    return s


n = int(input())

result1, result2 = set(), set()
for i in range(n):
    s = make_set(int(input()))
    if not i:
        result1 = result1 | s
    result1 &= s
    result2 |= s

print(len(result1))
print(*result1, sep='\n')
print(len(result2))
print(*result2, sep='\n')
