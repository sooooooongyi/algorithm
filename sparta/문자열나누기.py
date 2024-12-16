def solution(s):
    answer = 0
    pivot = s[0]
    diffCnt = 0
    sameCnt = 0

    for i in range(len(s)):
        if sameCnt == diffCnt:
            answer += 1
            diffCnt = 0
            sameCnt = 0
            pivot = s[i]
            
        if pivot == s[i]:
            sameCnt += 1
        else:
            diffCnt += 1
    
    return answer