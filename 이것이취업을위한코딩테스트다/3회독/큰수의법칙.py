# [구현] 난이도 1

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[N-1]
second = data[N-2]

answer = (M // (K+1)) * (K*first + second) + (M % (K+1))*first
print(answer)