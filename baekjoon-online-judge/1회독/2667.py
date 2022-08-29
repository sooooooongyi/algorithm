# DFS - 단지번호붙이기

N = int(input())
graph = []
num_list = []
result = 0
num = 0

def dfs(x,y):
    global num
    if x<= -1 or x >=N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        num += 1
        # 방문 한 곳은 0처리 (중복안되게끔)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for _ in range(N):
    graph.append(list(map(int, input())))

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            num_list.append(num)
            result += 1
            num = 0

print(result)
num_list.sort()

for i in range(len(num_list)):
    print(num_list[i])