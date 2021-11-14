from collections import deque
import sys

sys.setrecursionlimit(10000)

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    
    visited = [list(False for _ in range(w)) for _ in range(h)]

    count = 0
    queue = deque([])

    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and graph[i][j] == 1:
                queue.append([j, i])
                visited[i][j] = True

                while True:
                    x, y = queue.pop()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < w and 0 <= ny < h:
                            if visited[ny][nx] == False and graph[ny][nx] == 1:
                                visited[ny][nx] = True
                                queue.append([nx, ny])

                    if not queue:
                        count += 1
                        break
    print(count)