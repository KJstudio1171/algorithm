def solution(score):
    answer = []
    avg = []
    for i in score:
        avg.append(sum(i) / 2)
    for i in avg:
        rank = 1
        for j in avg:
            if i < j:
                rank += 1
        answer.append(rank)
    return answer