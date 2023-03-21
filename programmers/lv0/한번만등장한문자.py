def solution(s):
    answer = [[i, s.count(s[i])] for i in range(len(s))]
    answer = [s[i] for [i, j] in answer if j == 1]
    return ''.join(sorted(answer))