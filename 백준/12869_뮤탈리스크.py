import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

damage_list = [
    [9, 3, 1],
    [9, 1, 3],
    [3, 9, 1],
    [3, 1, 9],
    [1, 9, 3],
    [1, 3, 9]
]


def dfs(one, two, three, count):
    global result
    for damage in damage_list:
        x = 0 if one - damage[0] < 0 else one - damage[0]
        y = 0 if two - damage[1] < 0 else two - damage[1]
        z = 0 if three - damage[2] < 0 else three - damage[2]
        if x + y + z == 0:
            result = min(result, count + 1)
            return
        if count + 1 > result:
            return
        if dp[x][y][z] < count + 1:
            return
        else:
            dp[x][y][z] = count + 1
            dfs(x, y, z, count + 1)


n = int(input().rstrip())
scv = list(map(int, input().rstrip().split()))
for _ in range(3 - len(scv)):
    scv.append(0)
dp = [[[61] * 61 for _ in range(61)] for i in range(61)]
result = 61
dfs(scv[0], scv[1], scv[2], 0)
print(result)
