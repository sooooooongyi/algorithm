# DP - 포도주 마시기
# Solution
# (1) 풀었었던 계단 문제와 똑같이 접근 -> x
# (2) 포도주 문제는 계단 문제와 달리 안먹는 경우가 생김 (계단은 1계단 또는 2계단을 꼭 밟아야함) 포도주는 안마시고 저~ 먼데 먹어도 됨! 경우의 수 하나 추가 (기존 dp 값을 가져가는 경우) -> o

n = int(input())
arr = [0]
dp = [0 for _ in range(n+1)]

for _ in range(n):
    arr.append(int(input()))

dp[1] = arr[1]
if n>1:
    dp[2] = arr[1]+arr[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

print(max(dp))