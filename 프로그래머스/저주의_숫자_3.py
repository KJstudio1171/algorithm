def solution(n):
    l = [1] * n
    rep = 1
    while rep:
        rep = 0
        for i in range(len(l)):
            if (i + 1) % 3 == 0 and l[i] == 1:
                l[i] = 0
                l.append(1)
                rep = 1
            elif ((i + 1) % 10 == 3 or (i + 1) // 10 % 10 == 3) and l[i] == 1:
                l[i] = 0
                l.append(1)
                rep = 1
    answer = len(l)
    return answer