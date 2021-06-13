def make_dict(s: str) -> dict:
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result


wlen, slen = map(int, input().split())
w = input()
s = input()

d = make_dict(w)
dwindow = make_dict(s[0: wlen])

count = 0

# for i in range(slen - wlen + 1):
#     if s[i] in d and make_dict(s[i: i + wlen]) == d:
#         count += 1
# print(count)
