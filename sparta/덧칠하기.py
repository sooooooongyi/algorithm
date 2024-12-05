def solution(n, m, section):
    answer = 0
    idx = 0
    for i in range(len(section)):
        if idx < section[i]:
            idx = section[i] + m - 1
            answer += 1
        else:
            continue
    return answer