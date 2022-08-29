import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    if visited[v] == 1:
        return
    
    visited[v] = 1
    for i in graph[v]:
        dfs(i)


count = 0
for i in range(1, n+1):
    if visited[i] == 0:
        count += 1
        dfs(i)

print(count)