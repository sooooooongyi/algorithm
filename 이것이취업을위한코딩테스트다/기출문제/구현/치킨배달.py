import sys
from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 999999

houses = []
chicken = []

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      houses.append([i, j])
    elif graph[i][j] == 2:
      chicken.append([i, j])

for chick in combinations(chicken, M):
  tempResult = 0 # M개 조합에 대한 도시의 치킨거리
  for house in houses:
    count = 999999
    for i in range(M):
      count = min(count, abs(house[0] - chick[i][0]) + abs(house[1] -chick[i][1]))
    tempResult += count
  result = min(result, tempResult) # 최소의 도시의 치킨거리

print(result)