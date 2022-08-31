n = int(input())
data = list(map(int, input().split()))
answer = 0

data.sort()

for i in range(n):
  answer += data[i] * (n-i)

print(answer)