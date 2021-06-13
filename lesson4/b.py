import sys


def solution(text: str) -> str:
    d = {}
    result = []
    for word in text.split():
        if word not in d:
            result.append(0)
            d[word] = 1
        else:
            result.append(d[word])
            d[word] += 1
    return ' '.join(map(str, result))


text = sys.stdin.read()
print(solution(text))
