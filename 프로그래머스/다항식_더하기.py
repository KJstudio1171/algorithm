def solution(polynomial):
    l = [i.strip() for i in polynomial.split('+')]
    num = [0,0]
    for i in l:
        if i == 'x':
            num[0] += 1
        elif i[-1] == 'x':
            num[0] += int(i[:-1])
        else :
            num[1] += int(i)
    answer = ""
    if num[0] != 0:
        if num[0] != 1:
            answer += "%dx"%num[0]
        else :
            answer += "x"
    if num[1] != 0:
        if answer != "":
            answer += " + "
        answer += "%d"%num[1]
    return answer