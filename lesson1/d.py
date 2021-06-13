def solution(a: int, b: int, c: int):
    """This function solves sqrt(ax + b) = c equation."""
    if c < 0:
        return 'NO SOLUTION'
    if a:
        r = (c ** 2 - b) / a
        if r == int(r):
            return int(r)
        return 'NO SOLUTION'
    if b == c ** 2:
        return 'MANY SOLUTIONS'
    return 'NO SOLUTION'


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    print(solution(a, b, c))
