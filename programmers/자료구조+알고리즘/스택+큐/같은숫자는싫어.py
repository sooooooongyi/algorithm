def solution(arr):
    answer = [-1]
    for i in arr:
        if i == answer[-1]:
            continue
        else:
            answer.append(i)
    return answer[1:]