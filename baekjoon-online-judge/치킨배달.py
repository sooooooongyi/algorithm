import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

houses = []
shops = []
result = 9999

for i in range(N):
  for j in range(N):
    if data[i][j] == 1:
      houses.append([i, j])
    elif data[i][j] == 2:
      shops.append([i, j])

for shop in combinations(shops, M):
  temp = 0
  for house in houses:
    temp_len = 9999
    for i in range(M):
      temp_len = min(temp_len, abs(house[0]-shop[i][0]) + abs(house[1]-shop[i][1]))
    temp += temp_len
  result = min(result, temp)

print(result)  