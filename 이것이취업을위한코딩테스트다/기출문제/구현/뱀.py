n = int(input()) # 맵 크기
k = int(input()) # 사과 개수
data = [ [0] * (n+1) for _ in range(n+1)]
info = []

for _ in range(k):
  a, b = map(int, input().split())
  data[a][b] = 1

l = int(input()) # 회전 횟수
for _ in range(l):
  x, c = input().split()
  info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
  if c == 'L': # 'L' 일때 오른쪽으로 회전
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4 # 'D' 일때 왼쪽으로 회전
  return direction

def simulate():
  x, y = 1, 1
  data[x][y] = 2 # 뱀 몸통 2
  direction = 1
  time = 0
  index = 0

  q = [(x, y)] # 뱀이 차지하는 좌표

  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0)
        data[px][py] = 0
      if data[nx][ny] == 1:
        data[nx][ny] = 2
        q.append((nx, ny))
    else:
      time += 1
      break
    x, y = nx, ny
    time += 1
    if index < 1 and time == info[index][0]:
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())
