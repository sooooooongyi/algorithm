import sys
input = sys.stdin.readline

LIMIT_NUMBER = 46

N, M = map(int, input().split())
data = []

for i in range(1, LIMIT_NUMBER):
  for j in range(1, i+1):
    data.append(i)

print(sum(data[N-1:M]))