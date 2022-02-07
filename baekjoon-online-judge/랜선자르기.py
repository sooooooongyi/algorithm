import sys
input = sys.stdin.readline

K, N = map(int, input().split())
data = []

for _ in range(K):
  data.append(int(input()))

start = 1
end = max(data)

while start <= end:
  count = 0
  mid = (start + end) // 2
  for line in data:
    count += line // mid

  if count < N:
    end = mid - 1
  else:
    start = mid + 1

print(end)