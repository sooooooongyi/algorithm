def solution(A,B):
    answer = 0
    
    sortedA = sorted(A)
    reversedB = sorted(B, reverse = True)
    
    for i in range(len(A)):
        answer += sortedA[i] * reversedB[i]

    return answer