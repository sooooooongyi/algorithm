# 그리디 알고리즘 - 로프
# Solution
# (1) 로프 별 중량과, N이 주어졌을때 중량/N 해도 가장 작은 로프가 들 수 있어야하니까 가장 작은수 * N -> X
# (2) 임의로 N개 중 몇개만 빼도 된다! 문제 잘 읽어! 가능 무게는 (가장 작은 중량)*원소개수니까, 작은 순으로 하나씩 제거하며
# 중량*남은원소 개수가 가장 큰 값을 최대 무게로! -> O
N = int(input())
list = [int(input()) for _ in range(N)]
result = []

list.sort()
for i in range(N):
    result.append(list[i]*(N-i))

print(max(result))