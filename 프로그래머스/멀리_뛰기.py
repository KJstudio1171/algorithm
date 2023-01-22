def comb(n, m):
    num1 = 1
    num2 = 1
    for i in range(m):
        num1 *= (n - i)
    for i in range(1, m + 1):
        num2 *= i
    return num1 // num2


def solution(n):
    answer = 0
    m = 0
    while (n >= m):
        answer += comb(n, m)
        n -= 1
        m += 1
    return answer % 1234567
