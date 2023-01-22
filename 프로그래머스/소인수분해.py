def solution(n):
    answer = []
    prime = ['O'] * (n + 1)
    prime[0] = 'X'
    prime[1] = 'X'
    for i in range(2, n + 1):
        if prime[i] == 'O':
            for j in range(2, n // i + 1):
                prime[i * j] = 'X'
    for i,j in enumerate(prime):
        if j == 'O':
            if n % i == 0:
                answer.append(i)
    return answer