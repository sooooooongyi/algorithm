import sys
input = sys.stdin.readline
from collections import deque

DIRECTION_LENGTH = 8

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())

def bfs(x, y, endX, endY):
  q = deque()
  q.append([x, y])
  graph[x][y] = 1
  while q:
    x, y = q.popleft()
    if x == endX and y == endY:
      return graph[x][y]-1
    for i in range(DIRECTION_LENGTH):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < I and 0 <= ny < I:
        if graph[nx][ny] == 0:
          q.append([nx, ny])
          graph[nx][ny] = graph[x][y]+1

for _ in range(T):
  I = int(input())
  startX, startY = map(int, input().split())
  endX, endY = map(int, input().split())
  graph = [[0]*I for _ in range(I)]

  print(bfs(startX, startY, endX, endY))