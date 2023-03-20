def solution(array, n):
    count = len(array) + 1
    array.append(n)
    array.sort()
    if max(array) == n:
        return array[-2]
    if n - array[array.index(n) - 1] <= array[array.index(n) + 1] - n:
        return array[(array.index(n)-1)%count]
    return array[(array.index(n) + 1)%count]