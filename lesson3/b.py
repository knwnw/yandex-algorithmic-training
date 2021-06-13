from timeit import timeit


def intersection_slow(a: list, b: list) -> list:
    result = [num for num in set(a) if num in set(b)]
    return sorted(result)


def intersection_fast(a: list, b: list) -> list:
    a, b = set(a), set(b)
    result = [num for num in a if num in b]
    return sorted(result)


def intersection_fastest(a: list, b: list) -> list:
    return sorted(set(a) & set(b))


a = list(range(10))
b = list(range(10))

print(timeit('intersection_slow(a, b)',
             setup='from __main__ import intersection_slow, a, b'))
print(timeit('intersection_fast(a, b)',
             setup='from __main__ import intersection_fast, a, b'))
print(timeit('intersection_fastest(a, b)',
             setup='from __main__ import intersection_fastest, a, b'))
print(timeit('sorted(set(a).intersection(set(b)))',
             setup='from __main__ import a, b'))
