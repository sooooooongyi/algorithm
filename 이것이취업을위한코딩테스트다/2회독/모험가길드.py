n = int(input())
data = list(map(int, input().split()))

group_count = 0
data.sort()

count = 0
for i in data:
  count += 1
  if i <= count:
    group_count += 1
    count = 0

print(group_count)