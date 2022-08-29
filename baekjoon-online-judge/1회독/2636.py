import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []

def bfs():
  q = deque()
  q.append([0, 0])
  visited[0][0] = 1
  cnt = 0

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n  and 0 <= ny < m and visited[nx][ny] == 0:
        if graph[nx][ny] == 0:
          visited[nx][ny] = 1
          q.append([nx, ny])
        elif graph[nx][ny] == 1:
          graph[nx][ny] = 0
          visited[nx][ny] = 1
          cnt += 1
    answer.append(cnt)
    return cnt

timer = 0
while 1:
  timer += 1
  visited = [[0] * m for _ in range(n)]
  cnt = bfs()
  if cnt == 0:
    break

print(timer -1)
print(answer[-2])