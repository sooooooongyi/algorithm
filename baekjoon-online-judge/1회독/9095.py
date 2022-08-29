# DP - 1, 2, 3 더하기
# Solution
# (★) 1, 2, 3의 가짓수와 방법을 나열 해보면 기존 앞에 3개 원소의 갯수를 더한것과 같다는걸 이용
# 이를 미리 11까지 계산해두고, 필요한 값을 입력받아 출력 -> O
dp = [1, 2, 4]

for i in range(3, 11):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

t = int(input())
for i in range(t):
    print(dp[int(input())-1])