N, M = map(int, input().split())
graph = [0] * (M+1)
answer = N * (N-1) // 2

data = list(map(int, input().split()))

for i in data:
    graph[i] += 1

for j in graph:
    answer -= j * (j-1) // 2
  
print(answer)