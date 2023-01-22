def solution(n):
    data = 1
    for i in range(1, n + 2):
        data *= i
        if data > n:
            return i - 1
    return 0