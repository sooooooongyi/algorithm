import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9

houses = []
chicken = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      houses.append([i, j])
    if graph[i][j] == 2:
      chicken.append([i, j])

for chick in combinations(chicken, m):
  city_length = 0
  for house in houses:
    house_length = 1e9
    for i in range(m):
      house_length = min(house_length, abs(house[0] - chick[i][0]) + abs(house[1] - chick[i][1]))
    city_length += house_length
  answer = min(answer, city_length)

print(answer)