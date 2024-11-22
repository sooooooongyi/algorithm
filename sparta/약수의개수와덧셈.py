def countDivisor(divisor):
    count = 1 # 자기 자신
    for i in range(1, divisor // 2 + 1):
        if divisor % i == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if countDivisor(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer