n, m = map(int, input().split())
graph = []

for _ in range(n):
  graph.append(min(list(map(int, input().split()))))

print(max(graph))