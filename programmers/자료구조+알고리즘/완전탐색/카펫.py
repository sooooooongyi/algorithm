def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(2, total + 1):
        if total % i != 0:
            continue
        if total // i > i:
            continue
        if (i-2) * (total // i - 2) == yellow:
            answer = [i, total // i]
    return answer