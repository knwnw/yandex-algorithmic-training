def solution(a: list, target: int) -> str:
    left, right = 0, len(a) - 1
    while left <= right:
        m = (left + right) // 2
        if a[m] < target:
            left = m + 1
        elif a[m] > target:
            right = m - 1
        else:
            return 'YES'
    return 'NO'
