import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [list(map(int, input().split())) for _ in range(n)]

answer = 1
graph[x][y] = 2

while True:
    # 4방향 중 하나라도 벽이 아니라면 False
    check = False
    for i in range(4):
        d = (d+3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if graph[nx][ny] == 0:
            answer += 1
            graph[nx][ny] = 2
            x = nx
            y = ny
            check = True
            # 벽이 아닌 방향을 우선적으로 만나면 그 방향으로 가야함!
            break

    if not check:
        if graph[x-dx[d]][y-dy[d]] == 1:
            break
        else:
            x = x - dx[d]
            y = y - dy[d]

print(answer)
