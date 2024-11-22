def solution(n):
    numberStr = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        numberStr += str(mod)
        
    return int(numberStr, 3)