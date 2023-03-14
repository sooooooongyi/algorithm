def solution(slice, n):
    answer = n // slice
    return answer + 1 if n % slice else answer