n, k = map(int, input().split())

result = 0

while True:
    target = (n//k) * k
    result += (n - target)
    # 무조건 k의 배수가 되도록, 1씩 먼저 빼기
    n = target
    if n < k :
        break
    result += 1
    n //= k
    # 근데 남았으면 이제 나눗셈 한번

result += (n-1)
# 1이 될때 까지 또 뺄셈한 횟수 추가
print(result)