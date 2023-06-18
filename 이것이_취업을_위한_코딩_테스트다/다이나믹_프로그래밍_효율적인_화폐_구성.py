n, m = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

d = [0] * (m + 1)
for i in coin:
    d[i] = 1
for i in range(m + 1):
    for j in coin:
        if i - j >= 0 and d[i - j]:
            if d[i]:
                d[i] = min(d[i], d[i - j] + 1)
            else:
                d[i] = d[i - j] + 1
print(d)
