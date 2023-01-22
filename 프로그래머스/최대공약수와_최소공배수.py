def solution(n, m):
    a,b = max(n,m), min(n,m)
    while (a % b):
        a,b = b, a % b
    return [b, n * m / b]