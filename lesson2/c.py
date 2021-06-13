def solution(a: list, x: int) -> int:
    min_dist = abs(a[0] - x)
    idx = 0
    for i in range(1, len(a)):
        if abs(a[i] - x) < min_dist:
            min_dist = abs(a[i] - x)
            idx = i
    return a[idx]
