import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
graph = [0]*11

for element in data:
	graph[element] += 1

result = (N * (N + 1))//2
for element in graph:
	result -= element * (element + 1)//2

print(result)
