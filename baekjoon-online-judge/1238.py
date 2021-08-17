# 다익스트라 알고리즘 - 파티
# Solution
# (1) 시간 초과 : 

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[]for i in range(n+1)]
ans = [0] * (n+1)
heap = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkatra(start):
    distance = [INF] * (n+1)
    heapq.heappush(heap, [0, start]) # 비용, 노드
    distance[start] = 0

    while heap:
        c, n = heapq.heappop(heap)
        for nc, nn in graph[n]:
            nc += c
            if nw < distance[nn]:
                distance[nn] = nw
                heapq.heappush(heap, [nw, nn])
    return distance

for i in range(1, n+1):
    distance = dijkatra(i)
    ans[i] += distance[x]
    distance = dijkatra(x)
    ans[i] += distance[i]

print(max(ans))


'''
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now]+j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

for i in range(1, n+1):
    dijkstra(i)
    go_arr.append(distance[x])
    distance = [INF for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

dijkstra(x)

max_value = -1
for i in range(1, n+1):
    if go_arr[i]+distance[i] > max_value:
        max_value = go_arr[i]+distance[i]

print(max_value)
'''

