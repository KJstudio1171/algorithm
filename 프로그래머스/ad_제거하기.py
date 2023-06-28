def solution(strArr):
    l = []
    for i in strArr:
        if "ad" not in i:
            l.append(i)
    return l