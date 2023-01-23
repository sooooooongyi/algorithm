# [구현] 난이도1

N, M = map(int, input().split())
answer = 0

for _ in range(N):
  list = map(int, input().split())
  min_value = min(list)
  answer = max(answer, min_value)

print(answer)