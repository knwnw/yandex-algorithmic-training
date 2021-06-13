n, m = map(int, input().split())

anya = {int(input()) for _ in range(n)}
borya = {int(input()) for _ in range(m)}
print()

intersection = anya & borya
print(len(intersection))
print(*sorted(intersection))

anya_minus_borya = anya - borya
print(len(anya_minus_borya))
print(*sorted(anya_minus_borya))

borya_minus_anya = borya - anya
print(len(borya_minus_anya))
print(*sorted(borya_minus_anya))
