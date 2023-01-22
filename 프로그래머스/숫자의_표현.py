def solution(n):
    answer = 0
    for i in range(1, n + 1):
        for j in range(n):
            if (i + i + j) * (j + 1) / 2 == n:
                answer += 1
            elif (i + i + j) * (j + 1) / 2 >= n:
                break
    return answer