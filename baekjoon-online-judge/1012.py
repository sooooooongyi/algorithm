# dfs - 유기농 배추
# Solution
# (1) 풀이 방법은 맞았지만, 아직 풀이에 미숙ㅜ x, y의 방향 잘 파악!
# (2) 파이썬은 정해져있는 재귀의 깊이가 있음 -> 미리 정해둬야함
# (3) sys.setrecursionlimit()으로 해결 -> o

import sys
sys.setrecursionlimit(5000)
T = int(input())

def dfs_cabbage(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if (0<=nx<N) and (0<=ny<M):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs_cabbage(nx, ny)      

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    result = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                dfs_cabbage(i, j)
                result += 1
    
    print(result)