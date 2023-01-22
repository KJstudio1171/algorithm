def combination(a,b):
    num1 = 1
    num2 = 1
    for i in range(b):
        num1 *= (a - i)
    for i in range(1, b + 1):
        num2 *= i
    return num1 // num2


def solution(balls, share):
    return combination(balls, share)