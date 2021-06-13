def solve(k: int) -> set:
    """Solves the equation: |x| + |y| = k."""
    result = set()
    for v in range(-k, k + 1):
        result.add((v, k - abs(v)))
        result.add((v, -k + abs(v)))
    return result


def gps(coord: tuple, d: int) -> set:
    pass
