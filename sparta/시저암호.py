def solution(s, n):
    answer = []
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for word in s:
        if word == ' ':
            answer.append(' ')
        elif word in low:
            idx = low.find(word) + n
            answer.append(low[idx % 26])
        else:
            idx = up.find(word) + n
            answer.append(up[idx % 26])
    return "".join(answer)       