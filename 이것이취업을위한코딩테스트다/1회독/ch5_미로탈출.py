# [DFS/BFS] BFS
# 유효 조건을 꼭꼭 확인하자..!

from collections import deque

n, m = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                continue
            if graph[nx][ny]:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
            else:
                continue
    return graph[n-1][m-1]

print(bfs(0, 0))