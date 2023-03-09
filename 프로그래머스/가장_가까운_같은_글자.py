def solution(s):
    alpha = [-1] * 200
    answer = []
    for i,j in enumerate(s):
        if alpha[ord(j)] == -1:
            answer.append(-1)
            alpha[ord(j)] = i
        else :
            answer.append(i - alpha[ord(j)])
            alpha[ord(j)] = i
    return answer