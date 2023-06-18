import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
m, n = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(row, col):
    if row == m - 1 and col == n - 1:
        return 1
    if dp[row][col] != -1:
        return dp[row][col]
    tmp = 0
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < m and 0 <= nc < n and map_list[row][col] > map_list[nr][nc]:
            tmp += dfs(nr, nc)
    dp[row][col] = tmp
    return tmp


print(dfs(0, 0))
