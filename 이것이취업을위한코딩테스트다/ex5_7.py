# [DFS/BFS] 인접 리스트 
# 2차원 배열이 사용된다
# C++나 자바에서는 링크트리스트 표준 라이브러리를 사용하지만 파이썬은 list를 사용한다

graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)