# DP - 가장 긴 수열
# Solution
# (1) 유명한 문제! 이중 for문을 돌면서, 정렬대로 이어지면 +1 (이전과 비교) -> o

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))