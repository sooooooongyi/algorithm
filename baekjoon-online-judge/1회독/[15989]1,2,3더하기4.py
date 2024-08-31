# 🌜, ✨ DP 문제! 2, 3에 대한 점화식

t = int(input())
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i-2]
    
for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])