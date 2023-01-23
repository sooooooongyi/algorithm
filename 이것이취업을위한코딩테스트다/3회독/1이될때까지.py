# [구현] 난이도1

N, K = map(int, input().split())
answer = 0

while True:
  target = (N // K) * N
  answer += (N - target)
  N = target

  if N < K:
    break

  N //= K
  answer += 1

answer += N - 1
print(answer)