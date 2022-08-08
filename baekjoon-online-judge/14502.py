import sys 
import copy 
from collections import deque
from itertools import combinations

input = sys.stdin.readline 

dx = [0, 0, -1, 1] 
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))
answer = 0
q = deque()

def bfs():
  global answer
  copyGraph = copy.deepcopy(graph)
  for i in range(N):
    for j in range(M):
      if copyGraph[i][j] == 2:
        q.append([i, j])

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if copyGraph[nx][ny] == 2:
          copyGraph[nx][ny] = 2
          q.append([nx, ny])

  cnt = 0
  for i in copyGraph:
    cnt += i.count(0)

  answer = max(answer, cnt)

def wall():
  for a, b, c in combinations(graph, 3):
    print(a)
    print(b)
    print(c)

wall()
print(answer)
