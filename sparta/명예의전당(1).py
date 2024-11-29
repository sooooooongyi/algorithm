def solution(k, score):
    rank = []
    result = []
    
    for i in range(len(score)):
        rank.append(score[i])
        rank.sort(reverse = True)
        if i < k:
            result.append(rank[-1])
        else:
            result.append(rank[k-1])
    return result