def solution(s):
    answer = 0
    for i in s:
        if i == "(":
            answer += 1
        if i == ")":
            answer += -1
        if answer < 0:
            return False
        
    return answer == 0