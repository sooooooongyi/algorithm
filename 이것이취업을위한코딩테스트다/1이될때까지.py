# 1을 빼는것보다 나누는 것이 훨씬 더 빨리 1에 도달할 수 있다.

n, k = map(int, input().split())

while True:
    target = (n//k)*k
    result = (n-target)

    if n < k:
        break

    result += 1
    n = n // k

result += (n-1)
print(result)