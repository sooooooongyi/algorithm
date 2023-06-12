def solution(n, lost, reserve):
    newLost = list(set(lost) - set(reserve))
    newReserve = list(set(reserve) - set(lost))
    answer = len(newLost)
    
    for i in range(len(newLost)):
        if newLost[i] - 1 in newReserve:
            answer -= 1
            newReserve.remove(newLost[i] - 1)
            continue
        if newLost[i] + 1 in newReserve:
            answer -= 1
            newReserve.remove(newLost[i] + 1)
            continue
            
    return n - answer