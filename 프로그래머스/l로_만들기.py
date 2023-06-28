def solution(myString):
    l = []
    for i in myString:
        if ord(i) < ord('l') :
            l.append('l')
        else:
            l.append(i)
    return "".join(l)