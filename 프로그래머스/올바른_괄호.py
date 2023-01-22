def solution(s):
    num = 0
    for i in s:
        if num < 0:
            return False
        if i == '(':
            num += 1
        else :
            num -= 1
    return num == 0