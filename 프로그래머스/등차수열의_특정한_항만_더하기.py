def solution(a, d, included):
    answer = 0
    for i,v in enumerate(included):
        if v == True:
            answer += (a + i * d)
    return answer