def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    boxNum = len(score) // m
    for i in range(1, boxNum + 1):
        answer += score[i * m - 1] * m
    return answer