import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
visited = [[0] * M for _ in range(N)]
graph = []
count = 0

for i in range(N):
	graph.append(list(sys.stdin.readline().rstrip()))

for i in graph:
	if i == ".":
		count += 1

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y):
	queue = deque()
	queue.append([x, y])

	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if x == N -1 and y == M-1:
				break
			if 0<=nx<N and 0<=ny<M:
				if visited[nx][ny] == 0 and graph[nx][ny] == '.':
					visited[nx][ny] = visited[x][y] + 1
					queue.append([nx, ny])

bfs(0,0)
print(visited[N-1][M-1], (count - 1) * 2 - visited[N-1][M-1])