def GCD(i, j):
    while i % j != 0:
        i,j = j,i%j
        if not j :
            return 0
    return j


def solution(n):
    return n // GCD(n, 6) if GCD(n, 6) else 6 * n