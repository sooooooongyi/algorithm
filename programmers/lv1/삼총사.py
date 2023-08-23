from itertools import combinations

def solution(number):
    answer = 0
    combList = list(combinations(number, 3))
    for i in combList:
        if sum(i) == 0:
            answer += 1
            
    return answer