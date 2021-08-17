# [그리디] 큰수의 법칙

# 내 코드
# M이 K+1로 딱 떨어지지 않는 경우 답이 나오지 않음 -> ex 123 배열 5 3 답 3 3 3 2 3 -> 하지만 내 풀이는 3 3 3 2 2를 출력(mod와 나눗셈연산만 진행해서)
'''
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0

sum += max(arr)*(M//K)*K
arr.remove(max(arr))
sum += max(arr)*(M%K)

print(sum)
'''

# 해답 코드
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
result = 0

max_1 = max(arr)
arr.remove(max_1)
max_2 = max(arr)

# M/(K+1) = 한 세트가 들어가는 개수 * K = 한 세트당 max의 개수
count = int(M/(K+1))*K 
# 혹여나 남으면 최대값으로 채워줘야함
count += M % (K+1)

result += count*max_1
result += (M-count)*max_2

print(result)