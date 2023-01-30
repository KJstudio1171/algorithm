def chickenCal(chicken):
    ret = 0
    while(chicken > 0):
        tmp = chicken // 10
        if tmp == 0:
            break
        ret += tmp
        chicken %= 10
        chicken += tmp
    return ret

def solution(chicken):
    answer = chickenCal(chicken)
    return answer