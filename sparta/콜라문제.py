def solution(a, b, n):
    answer = 0
    while n >= a:
        cnt = (n // a) * b
        n = n % a + cnt
        answer += cnt
    return answer