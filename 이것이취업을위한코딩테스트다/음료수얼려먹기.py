n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 최종적으로 덩어리 개수를 셀 변수
result = 0
# 이중 for문을 돌면서, i,j로 부터 연결된 상하좌우를 계산
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

# 재귀적으로 호출. 상하좌우가 틀을 벗어나거나, 이미 방문중이라면 이어져있는지 탐색 중지
def dfs(x, y):
    if x<= -1 or x>=n or y<=-1 or y >=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False