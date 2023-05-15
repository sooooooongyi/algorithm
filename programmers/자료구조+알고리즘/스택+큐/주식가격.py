def solution(prices):
    answer = []
    length = len(prices)
    
    for i in range(length):
        sec = 0
        for j in range(i, length-1):
            if prices[i] <= prices[j]:
                sec += 1
            else:
                break
        answer.append(sec)
    return answer