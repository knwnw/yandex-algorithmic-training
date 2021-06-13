def solution(n: int, word: str) -> str:
    d = {}
    for _ in range(n):
        key, value = input().split()
        d[key] = value

    if word in d.keys():
        return d[word]
    if word in d.values():
        for key, value in d.items():
            if value == word:
                return key
