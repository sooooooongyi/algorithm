# 두 포인터 - 수들의 합2
N, M = map(int,input().split())
list = list(map(int, input().split()))

start = 0
end = 0
result = 0
sum = 0

for start in range(N):
    while sum<M and end<N:
        sum += list[end]
        end += 1
    if sum==M:
        result +=1
    sum -= list[start]
    # 이제 start가 1증가해서, 구간 합에서 start의 index는 빠져야하니까!

print(result)