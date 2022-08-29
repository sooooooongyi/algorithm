# DP - 계단 오르기
# Solution
# (1) 연속 3계단은 안됨에 대해 잘못 이해함.. 
# (2) 1계단을 올라오는 경우는 2+1로 올라오고, 2계단은 세 계단 연속을 신경쓰지 않아도됨 -> o

n = int(input())
arr = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(n):
    arr[i] = int(input())

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])

for i in range(3, n):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

print(dp[n-1])