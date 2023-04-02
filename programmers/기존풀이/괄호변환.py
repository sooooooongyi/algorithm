def divide(w):
    open = 0
    close = 0
    
    for i in range(len(w)):
        if w[i] == '(':
            open += 1
        else:
            close += 1
        if open == close:
            return w[:i + 1], w[i + 1:]
 
def isRightStr(u):
    stack = []
    
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
            
    return True
 
def solution(w):
    if not w:
        return ""
  
    u, v = divide(w)

    if isRightStr(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
                
        return answer