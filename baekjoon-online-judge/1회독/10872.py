# 구현 - 팩토리얼
# Solution
# (1) 가장 간단하게 생각할 수 있는 1~n까지 반복문으로 곱하기

n = int(input())
sum = 1
for i in range(1, n+1):
    sum *= i
print(sum)