# [구현] 난이도2

N, M = map(int, input().split())
d = [[0] * M for _ in range(N)]

x, y, direction = map(int, input().split())
d[x][y] = 1

graph = []
for i in range(N):
  graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

answer = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  if d[nx][ny] == 0 and graph[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    answer += 1
    turn_time = 0
    continue
  else:
    turn_time += 1

  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if graph[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(answer)