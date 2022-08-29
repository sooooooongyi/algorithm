# DP - 2*n 타일링
# Solution
# (1) f(n) = f(n-1) + f(n-2) 점화식 -> o 

dp = [0, 1, 2, 3]

for i in range(4, 1001):
    dp.append(dp[i-1]+dp[i-2])

n = int(input())
print(dp[n]%10007)