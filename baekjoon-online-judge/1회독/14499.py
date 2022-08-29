from __future__ import barry_as_FLUFL
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dice = [0, 0, 0, 0, 0, 0]


def rolling(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    if direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    if direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    if direction == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


commands = list(map(int, input().split()))

nx, ny = x, y
for command in commands:
    nx = x + dx[command-1]
    ny = y + dy[command-1]
    if 0 <= nx < n and 0 <= ny < m:
        rolling(command)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[-1]
        else:
            dice[-1] = graph[nx][ny]
            graph[nx][ny] = 0
        x, y = nx, ny
    else:
        continue
    print(dice[0])
