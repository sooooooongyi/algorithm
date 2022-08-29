# 구현 - 검증수

arr = list(map(int, input().split()))
square = [i*i for i in arr]
print(sum(square)%10)