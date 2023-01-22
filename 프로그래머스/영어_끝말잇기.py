def solution(n, words):
    for i, j in enumerate(words):
        if not i:
            continue
        if j[0] != words[i - 1][-1]:
            return [i % n + 1, i // n + 1]
        for k in words[:i]:
            if k == j:
                return [i % n + 1, i // n + 1]
    return [0, 0]