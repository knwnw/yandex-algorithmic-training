def solution():
    n = int(input())
    s = set()
    for _ in range(n):
        x, _ = map(int, input().split())
        s.add(x)
    return len(s)


print(solution())
