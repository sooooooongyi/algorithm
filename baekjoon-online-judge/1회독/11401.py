# 수학 - 이항 계수 3
# Solution
# (1) 그냥 이항 계수 팩토리얼 사용 -> 시간초과
# (2) 페르마의 소정리 (1000000007가 소수인걸 이용)
import sys
import math

n, k = map(int, sys.stdin.readline().split())

