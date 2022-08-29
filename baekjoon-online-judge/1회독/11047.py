# 그리디 알고리즘 - 동전 0
N, K = map(int, input().split())
list = []
count = 0

for i in range(N):
    list.append(int(input()))

for j in range(N):
    if(K == 0):
        break
    count += K//list[N-j-1]
    K %= list[N-j-1]

print(count)