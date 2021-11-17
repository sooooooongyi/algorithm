import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def general_dfs(x, y, color):
    for index in range(4):
        nx = x + dx[index]
        ny = y + dy[index]

        if 0 <= nx < n and 0 <= ny < n:
            if general_visited[nx][ny] == 0 and graph[nx][ny] == color:
                general_visited[nx][ny] = 1
                general_dfs(nx, ny, color)

def blind_dfs(x, y, color):
    for index in range(4):
        nx = x + dx[index]
        ny = y + dy[index]

        if 0 <= nx < n and 0 <= ny < n:
            if blind_visited[nx][ny] == 0 and graph[nx][ny] == color:
                blind_visited[nx][ny] = 1
                blind_dfs(nx, ny, color)

n = int(input())
graph = []

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

general_visited = [[0]*n for _ in range(n)]
blind_visited = [[0]*n for _ in range(n)]

for _ in range(n):
    graph.append(list(input()))

general_count = 0
blind_count = 0
for i in range(n):
    for j in range(n):
        if general_visited[i][j] == 0:
            general_count += 1
            general_dfs(i, j, graph[i][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if blind_visited[i][j] == 0:
            blind_count += 1
            blind_dfs(i, j, graph[i][j])

print(general_count, blind_count)