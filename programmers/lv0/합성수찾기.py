import math

def solution(n):
    answer = []
    for i in range(4, 101):
        for j in range (2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                answer.append(i)
                break
    return len([i for i in answer if i <= n])