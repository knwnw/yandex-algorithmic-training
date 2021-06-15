def find_left_x(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
        return ans


def find_right_x(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
        return ans


def find_max1(seq):
    ans = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > ans:
            ans = seq[i]
    return ans


def find_max2(seq):
    ans = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[ans]:
            ...
    return ...


def find_two_maxs(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(2, len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]
    return max1, max2


def find_min_even(seq):
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ans == -1 or seq[i] < ans):
            ans = seq[i]
    return ans


def short_words1(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(words)
    ans = ''
    for word in words:
        if len(word) == minlen:
            ans += word + ' '
    return ans


def short_words2(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(words)
    ans = []
    for word in words:
        if len(word) == minlen:
            ans.append(word)
    return ' '.join(ans)


def rle(s):
    pass
