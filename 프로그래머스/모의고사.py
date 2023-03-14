def solution(answers):
    answer = []
    case_1 = [1,2,3,4,5]
    case_2 = [2,1,2,3,2,4,2,5]
    case_3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    for i,j in enumerate(answers):
        if case_1[i % 5] == j:
            score[0] += 1
        if case_2[i % 8] == j:
            score[1] += 1
        if case_3[i % 10] == j:
            score[2] += 1
    for i,j in enumerate(score):
        if j == max(score):
            answer.append(i + 1)
    return answer