import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

array.sort()

answer = 0
group = 0

for i in array:
  group += 1
  if group >= i:
    answer += 1
    group = 0

print(answer)