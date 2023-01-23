# [정렬] 난이도1

N = int(input())
data = []
for _ in range(N):
  data.append(int(input()))

data = sorted(data, reverse=True)

for i in data:
  print(i, end=' ')