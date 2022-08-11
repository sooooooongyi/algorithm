# 아기 상어: 구현, 시뮬레이션, BFS
# - 현재 상어의 위치에서 물고기까지의 거리를 BFS로 구한다.
# - 먹을 수 있는 물고기가 없을 때 까지!

import sys
from collections import deque
input = sys.stdin.readline

INF = 1e9
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
now_x, now_y = 0, 0
size = 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0


def bfs():
    distance = [[-1] * n for _ in range(n)]
    q = deque([(now_x, now_y)])
    distance[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] == -1 and size >= graph[nx][ny]:
                    q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
    return distance


def find(distance):
    x, y = 0, 0
    min_distance = INF
    for i in range(n):
        for j in range(n):
            if distance[i][j] != -1 and 0 < graph[i][j] < size:
                if distance[i][j] < min_distance:
                    x, y = i, j
                    min_distance = distance[i][j]
    if min_distance == INF:
        return None
    else:
        return x, y, min_distance


answer = 0
ate = 0
while True:
    result = find(bfs())
    if result == None:
        print(answer)
        break
    else:
        now_x, now_y = result[0], result[1]
        answer += result[2]
        graph[now_x][now_y] = 0
        ate += 1
    if ate >= size:
        size += 1
        ate = 0
