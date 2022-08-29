# bfs - 미로 탐색

from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
                # 만약 벗어났다면!
            if graph[nx][ny] == 0:
                continue
                # 갈 수 없는 곳이라면!
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                # 만약 갈 수 있는 곳이라면, 비용 추가! (마지막까지 덮어쓸꺼임)
                queue.append((nx,ny))
                # 새로운 출발지 입력
    return graph[N-1][M-1]

print(bfs(0,0))