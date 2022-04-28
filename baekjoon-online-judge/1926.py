import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0] * m for _ in range(n)]
result = 0
max_count = 0

def bfs(x, y):
  q = deque()
  q.append([x, y])
  visited[x][y] = 1
  cnt = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
        if graph[nx][ny] == 0:
          continue
        else:
          q.append([nx, ny])
          visited[nx][ny] = 1
          cnt += 1
  return cnt

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and not visited[i][j]:
      result += 1
      max_count = max(max_count, bfs(i, j))

print(result)
print(max_count)