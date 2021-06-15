def find_range_of_flat_numbers(m: int, p: int,
                               n_flats_per_floor: int) -> tuple:
    minimal = (p - 1) * m * n_flats_per_floor + 1
    maximal = p * m * n_flats_per_floor
    return minimal, maximal


def solution(k1: int, m: int, k2: int, p2: int, n2: int) -> str:
    if n2 - 1 == 0:
        return k2 / n2, '+inf'
    else:
        return k2 / n2, k2 / (n2 - 1)


print(solution(89, 20, 41, 1, 11))
print(solution(11, 1, 1, 1, 1))
print(solution(3, 2, 2, 2, 1))
print(solution(11, 2, 4, 1, 2))
