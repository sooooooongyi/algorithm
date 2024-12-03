def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    
    for i in range(len(score)//m):
        arr = score[i*m:i*m+m]
        answer += arr[-1] * m
    
    return answer