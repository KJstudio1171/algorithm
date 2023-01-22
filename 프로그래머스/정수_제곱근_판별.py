import math

def solution(n):
    return (int(math.sqrt(n)) + 1) ** 2 if (int(math.sqrt(n)) * int(math.sqrt(n)) == n) else -1