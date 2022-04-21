# [DFS/BFS] DFS

n, m = map(int, input().split())
graph = []
count = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 이 함수에서 이어져있는 얼음들은 다 1 처리 -> i, j여도 부하가 크지 않음!
def dfs(x, y):
    if x <= -1 or y <= -1 or x >=n or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)

        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)   