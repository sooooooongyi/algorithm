import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[]for i in range(n+1)]
visited = [False] * (n+1)

distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node() :
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    # 자기 자신으로 갈땐 비용이 0
    visited[start] = True
    # 자기 자신은 이미 방문 노드고
    for j in graph[start]:
        distance[j[0]] = j[1]
        # 처음 시작 노드와 연결된 노드들은 일단 거리 입력
    for i in range(n-1):
        now = get_smallest_node()
        # 그중 가장 작은 노드의 index를 가져오고
        visited[now] = True
        # 방문!
        for j in graph[now]: # 방문한 노드들도 지네들 끼리 연결되있는게 있을꺼고
            cost = distance[now]+j[1] # 일단 cost로 계산해두고
            if cost < distance[j[0]]: # 기존 비용보다 작으면
                distance[j[0]] = cost # 갱신!
                
dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])