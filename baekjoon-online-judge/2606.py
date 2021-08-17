# DFS - 바이러스
# Solution
# (1) 양방향 그래프! -> o

N = int(input())
K = int(input())
graph = []
visited = [False]*N

for i in range(K):
    nodeFrom, nodeTo = map(int, input().split())
    graph.append([nodeTo, nodeFrom])
    graph.append([nodeFrom, nodeTo])

def dfs_virus(graph, nodeFrom, visited):
    if visited[nodeFrom-1]:
        return
    else:
        visited[nodeFrom-1] = True
    for i in range(len(graph)):
        if graph[i][0] == nodeFrom:
            if not visited[graph[i][1]-1]:
                dfs_virus(graph, graph[i][1], visited)


dfs_virus(graph, 1, visited)

count = 0
for i in range(N):
    if visited[i]:
        count +=1

print(count-1)