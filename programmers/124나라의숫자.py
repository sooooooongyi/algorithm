def solution(n):
    answer = ''
    dataSet = [4, 1, 2]

    while(n):
        answer = dataSet[n%3] + answer
        if n%3 == 0:
            n = n//3 - 1
        else:
            n = n//3
    return answer