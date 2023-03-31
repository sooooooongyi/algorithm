def solution(num, total):
    n = (total - ((num -1) * num) // 2) // num
    return [i for i in range(n, n+num)]
