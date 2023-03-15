def solution(price):
    if price >= 500000:
        return price * 0.8 // 1
    if price >= 300000:
        return price * 0.9 // 1
    if price >= 100000:
        return price * 0.95 // 1
    return price