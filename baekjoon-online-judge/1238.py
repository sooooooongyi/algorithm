# 다익스트라 알고리즘 - 파티

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[]for i in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q, (0, start)) # 비용, 노드
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

result = [[]]
answer = []
for i in range(1, n+1):
    result.append(dijkstra(i))

for i in range(1, n+1):
    answer.append(result[i][x] + result[x][i])

print(max(answer))