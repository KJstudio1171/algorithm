n = int(input())

color_list = []
dp = [[999999999] * 3 for i in range(n)]
for _ in range(n):
    color_list.append(list(map(int, input().split())))
for i in range(3):
    dp[0][i] = color_list[0][i]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + color_list[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + color_list[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + color_list[i][2]

print(min(dp[n - 1]))
