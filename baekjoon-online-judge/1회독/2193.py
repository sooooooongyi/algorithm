# 구현 - 이친수
# Solution 
# (1) 이친수를 나열하고, 2의 제곱들의 덧셈으로 나타내보면 이친수의 조합이 직전 조합을 다 가지고 오는걸 확인. 즉 개수 상으론 피보나치 -> o

n = int(input())
dp = [1, 1]

for i in range(2, 91):
    dp.append(dp[i-1]+dp[i-2])

print(dp[n-1])