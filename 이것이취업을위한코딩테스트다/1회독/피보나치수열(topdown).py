d = [0] * 99
# 메모이제이션을 위한 리스트

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0
    # 만약 이미 계산된 적 있다면~ 그냥 return
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
print(fibo(99))