import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
V = int(input())

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(V):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        for i in range(1, N+1):
            if not visited[i] and graph[v][i]:
                q.append(i)
                visited[i] = True

bfs(1)

cnt = 0
for i in range(1, N+1):
    if visited[i] == True:
        cnt += 1

print(cnt-1)