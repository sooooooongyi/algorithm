def solution(n):
    for i in range(n, n*6+1):
        if i % n == 0 and i % 6 == 0:
            return i // 6