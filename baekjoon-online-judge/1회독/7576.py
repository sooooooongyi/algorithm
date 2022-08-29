# BFS - 토마토

from collections import deque

m, n = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
        
queue = deque()     
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
                queue.append((i,j))
bfs()

isTrue = False
result = -2
for i in graph:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)