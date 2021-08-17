# DFS & BFS
N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    for i in range(1, N+1):
        if not visited[i] and graph[v][i] == 1:
            # 방문하지 않았고, 연결되어있으면
            dfs(i)

def bfs(v):
    queue = [v]
    visited[v] = False
    while queue:
        v = queue.pop(0)
        print(v, end = ' ')
        for i in range(1, N+1):
            if visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = False

dfs(V)
print()
bfs(V)