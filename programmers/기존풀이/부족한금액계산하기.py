def solution(price, money, count):
    answer = -1
    total = price * count * (count + 1) / 2
    if total > money:
        answer = total - money
    else:
        answer = 0

    return answer