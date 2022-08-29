# DP - 1로 만들기
# Solution
# (1) 파이썬 문법 실수.. -> x
# (2) i가 3,2로 나뉘는지 아닌지를 효율적으로 어떻게 만드는감... -> o
dp = [1e9, 0, 1, 1]

for i in range(4, 1000001):
    if i%3==0:
        div_3 = i//3
    else:
        div_3 = 0

    if i%2==0:
        div_2 = i//2
    else:
        div_2 = 0

    dp.append(min(dp[div_3], dp[div_2], dp[i-1])+1)

n = int(input())
print(dp[n])