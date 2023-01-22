def GCD(a,b):
    while(a % b):
        a,b = b, a % b
    return b
        

def solution(a, b):
    num = b // GCD(a, b)
    while(num % 2 == 0):
        num //= 2
    while(num % 5 == 0):
        num //= 5
    return 1 if num == 1 else 2