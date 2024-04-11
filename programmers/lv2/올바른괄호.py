def solution(s):
    answer = True
    stack = 0
    
    for i in s:
        if i == '(':
            stack += 1
        if i == ')':
            stack -= 1
        if stack < 0:
            return False
            
    if stack == 0:
        return True

    return False