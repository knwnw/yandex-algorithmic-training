def solution(a: list) -> str:
    M1, M2, m1, m2 = 0, 0, 0, 0
    for i in range(len(a)):
        if a[i] > 0:
            if M1 <= a[i]:
                M2 = M1
                M1 = a[i]
            elif M2 <= a[i] <= M1:
                M2 = a[i]
        elif a[i] < 0:
            if m1 >= a[i]:
                m2 = m1
                m1 = a[i]
            elif m2 >= a[i] >= m1:
                m2 = a[i]
    # if M1 * M2 > m1 * m2 сломается на 1 0
    if M1 * M2 > m1 * m2:  # ломается на -1 0
        return f'{M2} {M1}'
    elif M1 * M2 < m1 * m2:
        return f'{m1} {m2}'
    # TODO: what to do when M1 * M2 == m1 * m2 == 0?


a = list(map(int, input().split()))
print(solution(a))
