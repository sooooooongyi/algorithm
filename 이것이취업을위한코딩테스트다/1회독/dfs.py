# 1~8번 노드에서 인접한 노드의 번호를 적어둠
# 노드[1] 이런식 (그래서 노드[0]을 비워둠)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 인덱스 0은 사용안하기 때문에 9개 정의, 0번 안씀
visited = [False]*9

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
dfs(graph, 1, visited)