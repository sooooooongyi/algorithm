def solution(n):
    n=n+1
    answer=[True]*n
    for i in range(2, int(n**0.5)+1):
        if answer[i] == True:
            for j in range(i+i, n, i):
                answer[j] = False
    a = [i for i in range(2, n) if answer[i]==True]
    return len(a)