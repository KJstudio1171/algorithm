import sys

n = int(sys.stdin.readline().rstrip())
store = list(map(int, sys.stdin.readline().rstrip().split()))
d = [0] * n

d[1] = max(d[0], store[1])

for i in range(2, n):
    d[i] = max(d[i - 1], store[i] + d[i - 2])

print(d[n - 1])
