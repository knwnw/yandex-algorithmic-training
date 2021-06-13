def solution(a: list) -> str:
    for i in range(1, len(a)):
        if a[i - 1] >= a[i]:
            return 'NO'
    return 'YES'
