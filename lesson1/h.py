def solution(interval1: int, n1: int, interval2: int, n2: int):
    # TODO: returns wrong answer.
    a1 = (interval1 + 1) * (n1 - 1) + 1
    b1 = a1 + 2 * interval1
    a2 = (interval2 + 1) * (n2 - 1) + 1
    b2 = a2 + 2 * interval2

    if a2 > b1 or a1 > b2:
        return -1
    left = a1 if a1 >= a2 else a2
    right = b1 if b1 <= b2 else b2
    return f'{left} {right}'


def lengths(interval: int, n_seen: int) -> tuple:
    min_length = (interval + 1) * (n_seen - 1) + 1
    max_length = min_length + 2 * interval
    return min_length, max_length


def intersection(a1: int, b1: int, a2: int, b2: int) -> str:
    if a2 > b1 or a1 > b2:
        return '-1'
    left = a1 if a1 >= a2 else a2
    right = b1 if b1 <= b2 else b2
    return f'{left} {right}'


print(solution(1, 3, 3, 2))
print(solution(1, 5, 1, 2))
