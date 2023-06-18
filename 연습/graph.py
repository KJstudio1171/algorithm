# 인접 리스트 방식
from collections import deque
graph_adjacency_list = [[],
                        [2, 3],
                        [1],
                        [1]]

# 인접 행렬 방식
INF = 999999999

graph_adjacency_matrix = [
    [],
    [0, 0, 1, 1],
    [0, 1, 0, INF],
    [0, 1, INF, 0]
]


def dfs_graph(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[v]:
            dfs_graph(graph, i, visited)


def bfs_graph(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[v]:
                queue.append(i)
                visited[i] = True
