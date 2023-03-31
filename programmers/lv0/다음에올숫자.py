def solution(common):
    answer = 0
    a = False # 등차수열
    b = False # 등비수열
    
    if common[2] - common[1] == common[1] - common[0]:
        a = True
    else:
        b = True
        
    if a:
        return common[-1] + (common[1] - common[0])
    if b:
        return common[-1] * (common[1] // common[0])