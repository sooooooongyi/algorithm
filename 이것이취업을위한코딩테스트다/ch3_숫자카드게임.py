# [그리디] 숫자카드게임

# 내 코드
N, M = map(int,input().split())
min_item = 0

for _ in range(N):
    items = list(map(int,input().split()))
    check = min(items)
    if min_item < check:
        min_item = check
    # 해답 코드 (나머지 부분은 같고 최솟값 찾는 로직만 다름)
    min_item = min(check, min_item)

print(min_item)