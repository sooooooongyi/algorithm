def solution(array):
    arr = [0] * (max(array) + 1)
    for i in array:
        arr[i] += 1
    return arr.index(max(arr)) if arr.count(max(arr)) == 1 else -1