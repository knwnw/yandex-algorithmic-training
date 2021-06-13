def solution(a: list):
    if len(a) == 1:
        return 0

    i, j = 0, len(a) - 1
    while i <= j:
        j = j - 1 if a[i] == a[j] else len(a) - 1
        i += 1
    return j


# print(solution([1, 2, 3, 2, 1]))
# print(solution([1, 2, 1, 2, 2]))
# print(solution([1, 2, 3, 4, 5]))

# for i in range(1, 8):
#     lst = list(range(1, i + 1))
#     sol = solution(lst)
#     print(lst, sol, lst[sol::-1])

for i in range(1, 6):
    lst = list(range(i))
    lst.extend([5, 6, 6, 5])
    sol = solution(lst)
    print(lst, sol, lst[sol-2::-1])
