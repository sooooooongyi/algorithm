def solution(n):
    answer = []
    for i in range(1, 11):
        factorial = 1
        for j in range(1, i+1):
            factorial *= j
        answer.append(factorial)
    return max([i+1 for i in range(10) if n >= answer[i]])