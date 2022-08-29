# 풀이법
# 1) DP보단 그리디에 가까운 문제
# 2) "여태 합보다 내 값이 더 크면 내 값을 append" 규칙

n = int(input())
graph = list(map(int, input().split()))

sum = [graph[0]]

for i in range(len(graph)-1):
  sum.append(max(sum[i]+graph[i+1], graph[i+1]))

print(max(sum))