def open_calculator(x: int, y: int, z: int, N: int) -> int:
    count = 0
    for digit in set(str(N)):
        if int(digit) not in {x, y, z}:
            count += 1
    return count


x, y, z = map(int, input().split())
N = int(input())

print(open_calculator(x, y, z, N))
