def solution(n):
    answer = [[0] * n for i in range(n) ]
    for i,v in enumerate(answer):
        v[i] = 1
    return answer