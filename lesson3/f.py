def make_pairs(g: str) -> list:
    return [g[i] + g[i + 1] for i in range(len(g) - 1)]


def count(g1: str, g2: str) -> int:
    result = 0
    g2 = set(make_pairs(g2))
    for pair in make_pairs(g1):
        if pair in g2:
            result += 1
    return result


g1, g2 = input(), input()
print(count(g1, g2))
