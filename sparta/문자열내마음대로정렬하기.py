def solution(strings, n):
    strings.sort() # 사전순
    return sorted(strings, key = lambda x : x[n])