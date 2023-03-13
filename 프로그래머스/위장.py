from collections import defaultdict
def solution(clothes):
    answer = 1
    d = defaultdict(int)
    for i in clothes:
        d[i[1]] += 1
    for i in d.values():
        answer *= (i + 1)
    answer -= 1
    return answer