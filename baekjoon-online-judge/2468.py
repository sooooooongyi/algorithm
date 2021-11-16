import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
answer = 0

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and graph[nx][ny] > h:
                visited[nx][ny] = 1 
                dfs(nx, ny, h)

for h in range(max(map(max, graph))):
    visited = [[0] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] > h:
                dfs(i, j, h)
                count += 1
    
    answer = max(answer, count)

print(answer)

