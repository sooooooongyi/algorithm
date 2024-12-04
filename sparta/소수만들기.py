from itertools import combinations, permutations

def isPrime(num):
    cnt = 1
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            cnt += 1
    return cnt

def solution(nums):
    result = 0
    perm = list(combinations(nums, 3))
    for i in perm:
        if isPrime(sum(i)) < 3:
            result += 1
    return result