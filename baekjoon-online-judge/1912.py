# DP - 연속합
# Solution
# (1) 연속된..수.. -> x
# (2) dp[i] = max(dp[i-1]+arr[i],arr[i]) -> x
# (3) index 문제 -> o

n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(1, n):
    dp.append(max(dp[i-1]+arr[i], arr[i]))

print(max(dp))