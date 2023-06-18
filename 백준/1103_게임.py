import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(row, column, count):
    global result

    result = max(count, result)
    dp[row][column] = count
    visited[row][column] = True

    board_num = int(board[row][column])
    for i in range(4):
        r = row + dr[i] * board_num
        c = column + dc[i] * board_num
        if 0 <= r < n and 0 <= c < m and board[r][c] != "H" and dp[r][c] < count + 1:
            if visited[r][c] == True:
                print(-1)
                exit()
            dfs(r, c, count + 1)
    visited[row][column] = False


n, m = map(int, input().split())
board = []
visited = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
result = 0
for i in range(n):
    board.append(list(input().rstrip()))
dfs(0, 0, 0)
print(result + 1)
