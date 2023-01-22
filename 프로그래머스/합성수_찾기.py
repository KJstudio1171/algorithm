def is_prime(n):
    if n == 1 or n ==2 or n==3:
        return True
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

def solution(n):
    return len([i for i in range(1, n + 1) if not is_prime(i)])