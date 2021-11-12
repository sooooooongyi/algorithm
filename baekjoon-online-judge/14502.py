# 브루트포스 + bfs
import sys 
import copy 
from collections import deque

input = sys.stdin.readline 

dx = [0,0,-1,1] 
dy = [1,-1,0,0]


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

q = deque()

def bfs():
    global answer
    # 바이러스가 있는 곳 = bfs 시작점
    copyGraph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if copyGraph[i][j] == 2:
                q.append([i, j])
    # bfs로 바이러스 시작점으로부터 퍼져나가는 시뮬레이션
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if copyGraph[nx][ny] == 0:
                    copyGraph[nx][ny] = 2
                    q.append([nx, ny])
    count = 0
    for i in copyGraph:
        # 안전 지대의 수 구하기
        count += i.count(0)
    answer = max(answer, count)

def wall(wallCnt):
    if wallCnt == 3:
        bfs()
        return
    # 빈 곳에 3개의 벽을 세우는 모든 경우의 수를 재귀로 구현 (브루트 포스)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(wallCnt+1)
                graph[i][j] = 0

# 벽 세워서 bfs까지 실행
wall(0)
print(answer)