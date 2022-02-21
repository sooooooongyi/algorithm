N, K = map(int, input().split())
data = [0] * (N+1)
cnt = 0

for i in range(2, N+1):
  if data[i] != 1:
    for j in range(i, N+1, i):
      if data[j] == 0:
        data[j] = 1
        cnt += 1
        if cnt == K:
          print(j)  