import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
  q = deque()
  visited = [False]*(n+1)
  result = [0]*(n+1)  

  q.append(v)
  visited[v] = True

  while q:
    current = q.popleft()
    for i in graph[current]:
      if not visited[i]:
        q.append(i)
        result[i] = result[current] + 1
        visited[i] = True

  return sum(result)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

answer = []
for i in range(1, n+1):
  answer.append(bfs(i))

print(answer.index(min(answer))+1)
