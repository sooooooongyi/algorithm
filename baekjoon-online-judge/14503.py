import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

answer = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

graph[x][y] = 2

while True:
    check = False
    for i in range(4):
        d = (d + 3)%4
        nx = x + dx[d]
        ny = y + dy[d]

        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            answer += 1
            x, y = nx, ny
            check = True
            break
    if not check:
        if graph[x - dx[d]][y - dy[d]] == 1:
            break
        else:
            x = x - dx[d]
            y = y - dy[d]

print(answer)
