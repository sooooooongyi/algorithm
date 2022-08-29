# 구현 - 이항 계수1
# Solution 
# (1) 그냥 내장 함수 쓰기 import math -> o
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
fact = [1, 1]
p = 1000000007

for i in range(2, n+1):
    fact.append(fact[i-1]*i%p)

def power(a, n, p):
    if n == 0:
        return 1
    result = power(a*a%p, n//2, p)
    if n&1:
        result = result*a%p
    return result

print(fact[n]*power(fact[k]*fact[n-k], p-2, p)%p) 