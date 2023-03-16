from itertools import combinations

def solution(numbers):
    return max([i * j for i, j in list(combinations(numbers, 2))])