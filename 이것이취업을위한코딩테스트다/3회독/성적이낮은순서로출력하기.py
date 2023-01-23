# [정렬] 난이도1
N = int(input())
data = []
for _ in range(N):
  input_data = input().split()
  data.append(input_data[0], input_data[1])

data = sorted(data, key = lambda student: student[1])
for i in range(N):
  print(i[0], end= ' ')