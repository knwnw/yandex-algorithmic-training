a, b, c = 1, 40, 2
d, e = 40, 1

sizes = [a, b, c]
length = len(sizes)

for el in sizes:
    if d >= el:
        sizes.pop(sizes.index(el))
        break
for el in sizes:
    if e >= el:
        sizes.pop(sizes.index(el))
        break

if len(sizes) == length - 2:
    print('YES')
else:
    print('NO')
