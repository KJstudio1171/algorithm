n = int(input())
price = list(map(int, input().split()))
dp = [0] * n

dp[0] = price[0]

for i in range(1, n):
    for index in range(i):
        if dp[index] > 0:
            dp[i] = max(dp[i], dp[i - index - 1] + price[index])
    dp[i] = max(dp[i], price[i])
print(dp[n - 1])
