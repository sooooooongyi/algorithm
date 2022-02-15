from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())
graph = []

for _ in range(H):
  temp = []
  for _ in range(N):
    temp.append(list(map(int,input().split())))
  graph.append(temp)


q = deque([])
for h in range(H):
  for y in range(N):
    for x in range(M):
      if graph[h][y][x] == 1:
        q.append([h, y, x])

while q:
  z, y, x = q.popleft()

  for i in range(6):
    nz = z + dz[i]
    ny = y + dy[i]
    nx = x + dx[i]

    if 0<=nx<M and 0<=ny<N and 0<=nz<H and graph[nz][ny][nx] == 0:
      q.append([nz, ny, nx])
      graph[nz][ny][nx] = graph[z][y][x] + 1

day = 0
for i in graph:
  for j in i:
    for k in j:
      # 0이 있다면 전부 익을 수 없는 상태
      if k == 0:
        print(-1)
        exit(0)
    day = max(day, int(max(j)))

print(day - 1)