import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  data = []
  for _ in range(N):
    first, second = map(int, input().split())
    data.append([first, second])

  count = 1 # 여기서 count는 통과된 사람!

  data.sort()
  max_data = data[0][1]
  for i in range(1, N):
    if max_data > data[i][1]:
      count += 1
      max_data = data[i][1]
  
  print(count)
