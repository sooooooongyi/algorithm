from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(graph, data):
  q = deque([data])
  visited = [[False]*5 for _ in range(5)]

  while q:
    x, y, d = q.popleft()
    visited[x][y] = True

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      nd = d + 1

      if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
        visited[nx][ny] = True

        if graph[nx][ny] == 'P':
          if nd <= 2:
            return False
        elif graph[nx][ny] == 'O':
          if nd == 1:
            q.append([nx, ny, nd])
  return True


def solution(places):
    answer = []
    for place in places:
      flag = 1
      for i in range(5):
        for j in range(5):
          if place[i][j] == 'P':
            result = bfs(place, [i, j, 0])
            if not result:
              flag = 0
      answer.append(flag)
    return answer