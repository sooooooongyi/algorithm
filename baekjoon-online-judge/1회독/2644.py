import sys
input = sys.stdin.readline

def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      result[i] = result[v] + 1
      dfs(i)


n = int(input())
p1, p2 = map(int, input().split())

m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = [0]*(n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(p1)

if result[p2]>0:
  print(result[p2])
else:
  print(-1)