def solution(lottos, win_nums):
    lottoCnt = 0
    zeroCnt = 0
    
    for i in range(6):
        if lottos[i] in win_nums:
            lottoCnt += 1
        if lottos[i] == 0:
            zeroCnt += 1
            
    if lottoCnt == 0 and zeroCnt == 0:
        return [6, 6]
    
    if lottoCnt == 0:
        return [7 - zeroCnt, 6]
    else:
        return [7 - (lottoCnt + zeroCnt), 7 - lottoCnt]