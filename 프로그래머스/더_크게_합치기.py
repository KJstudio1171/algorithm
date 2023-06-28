def solution(a, b):
    c1 = str(a) + str(b)
    c2 = str(b) + str(a)
    return int(c1) if int(c1) > int(c2) else int(c2)