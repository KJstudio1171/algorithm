def solution(myString):
    tmp = []
    tmp2 = ''
    for i in myString:
        if i == 'x':
            if tmp2 != '':
                tmp.append(tmp2)
                tmp2 = ''
            else:
                continue
        else:
            tmp2 += i
    if tmp2 != '':
        tmp.append(tmp2)
    return sorted(tmp)