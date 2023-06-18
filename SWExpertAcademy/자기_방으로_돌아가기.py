import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for i in range(t):
    n = int(input())
    hallway = [0] * 201
    for j in range(n):
        start, end = 0, 0
        n, m = map(int, input().split())
        if n % 2 == 0:
            start = n//2
        else:
            start = n // 2 + 1
        if m % 2 == 0:
            end = m // 2
        else:
            end = m // 2 + 1
        for k in range(min(start, end), max(start, end) + 1):
            hallway[k] += 1

    print(max(hallway))
