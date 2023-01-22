def solution(n,a,b):
    stack1 = list(range(1, n + 1))
    answer = 1
    i = 2
    while(i < n):
        for x in range(n // i):
            if a in stack1[i*x:i*(x+1)] and b in stack1[i*x:i*(x+1)]:
                return answer
        answer += 1
        i *= 2
    return answer