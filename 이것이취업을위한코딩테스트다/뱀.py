import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())

graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(K):
  x, y = map(int, input().split())
  graph[x][y] = 1

L = int(input())
L_list = []

for _ in range(L):
  X, C = input().split()
  L_list.append([int(X), C])

def turn(direction, c):
  if c == 'L':
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return direction

def simulation():
  x, y = 1, 1
  graph[x][y] = 2
  direction = 0
  time = 0
  index = 0
  q = [(x, y)]

  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx and nx <= N and 1 <= ny and ny <= N and graph[nx][ny] != 2:
      if graph[nx][ny] == 0:
        graph[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0)
        graph[px][py] = 0
    else:
      time += 1
      break

    x, y = nx, ny
    time += 1
    if index < L and time == L_list[index][0]:
      direction = turn(direction, L_list[index][1])
      index += 1
  return time

print(simulation())
