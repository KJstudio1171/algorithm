def solution(numLog):
    answer = ''
    tmp = 0
    for i in numLog:
        if i - tmp == 1:
            answer += 'w'
        elif i - tmp == 10:
            answer += 'd'
        elif i - tmp == -1:
            answer += 's'
        elif i - tmp == -10:
            answer += 'a'
        tmp = i
    return answer