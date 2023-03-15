import math

def solution(n):
    for i in range(1, n // 2 + 1):
        if (i**2) == n:
            return 1
    return 2