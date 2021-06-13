def solution(a: int, b: int, c: int) -> str:
    return 'YES' if (a + b > c) and (b + c > a) and (c + a > b) else 'NO'


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    print(solution(a, b, c))
