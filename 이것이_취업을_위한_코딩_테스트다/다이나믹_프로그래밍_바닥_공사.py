n = int(input())

d = [0] * 10001
d[1] = 1
d[2] = d[1] + 2
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])
