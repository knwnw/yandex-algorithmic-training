import sys


def solution(text: str):
    d = {}
    for word in text.split():
        d[word] = d.get(word, 0) + 1

    lst = []
    m = max(d.values())
    for word in d:
        if d[word] == m:
            lst.append(word)
    return min(lst)


text = sys.stdin.read()
print(solution(text))
