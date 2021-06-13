def solution(n: int, k: int, m: int) -> int:  # TODO: fix the solution
    if k < m:
        return 0
    count = 0
    while True:
        # TODO: бесконечный цикл при (1, 1, 3), (2, 1, 3), (2, 2, 3), (3, 1, 3)
        n = n - k
        if n < 0:
            break
        count += k // m
        n += k % m
    return count


if __name__ == '__main__':
    # n, k, m = map(int, input().split())
    # print(solution(n, k, m))

    for a in range(201):
        for b in range(201):
            for c in range(1, 201):
                solution(a, b, c)
