import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

answer = 0
temp = []

array.sort(reverse = True)

for i in range(N):
    if len(temp) >= array[i]:
      temp = []
      answer += 1
    else:
      temp.append(array[i])

print(answer)