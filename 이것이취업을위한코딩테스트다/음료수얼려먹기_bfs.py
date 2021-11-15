import collections 
import deque

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    if graph[x][y] == 1:
        return 0
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < x or 0 <= ny < y:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
    return 1

result = 0
for i in range(n):
    for j in range(m):
        result += bfs(i, j)

print(result)