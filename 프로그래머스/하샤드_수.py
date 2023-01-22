def solution(x):
    t = x
    num = 0
    while (x > 0) :
        num += x % 10
        x //= 10
    return t % num == 0