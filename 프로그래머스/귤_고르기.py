def solution(k, tangerine):
    d = {}
    answer = 0
    for i in tangerine:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    for j in sorted(list(d.values()),reverse=True):
        answer += 1
        k -= j
        if k <= 0 :
            break
    return answer