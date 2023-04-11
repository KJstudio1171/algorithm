def solution(k, score):
    answer = []
    l = []
    for i in score:
        if len(l) < k:
            l.append(i)
        else :
            if i > min(l):
                l.remove(min(l))
                l.append(i)
        answer.append(min(l))
    return answer