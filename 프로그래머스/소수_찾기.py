def solution(n):
    answer = 0
    l = [1] * (n + 1)
    l[0] = 0
    l[1] = 0
    for i in range(2, n + 1):
        tmp = i
        if l[i] == 1:
            answer += 1
        while tmp <= n:
            l[tmp] = 0
            tmp += i
    return answer