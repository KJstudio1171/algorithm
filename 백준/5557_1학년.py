import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
nums = list(map(int, input().split()))
result = 0
dp = [[0] * 21 for _ in range(101)]
dp[0][nums[0]] = 1

for i in range(1, n):
    for j in range(21):
        if dp[i - 1][j]:
            if j + nums[i] <= 20:
                dp[i][j + nums[i]] += dp[i - 1][j]
            if j - nums[i] >= 0:
                dp[i][j - nums[i]] += dp[i - 1][j]
print(dp[n - 2][nums[-1]])
