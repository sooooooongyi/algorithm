import sys
input = sys.stdin.readline

N, M = map(int, input().split())
money_list = []

for i in range(N):
  money_list.append(int(input()))

money_count = [10001] * (M+1)

# 🍀 풀이법
# - 점화식을 만들것. (n-1을 만들 수 있으면, n을 만들 수 있다.)
# - 1~M까지 만들 수 있는 최소한의 수를 저장하며 M의 값을 구한다.

for i in range(N):
  for j in range(money_list[i], M+1):
    if money_count[j - money_list[i]] != 10001:
      money_count[j] = min(money_count[j - money_list[i]]+1, money_count[j])

if money_count[M] == 10001:
  print(-1)
else:
  print(money_count[M])