import math 

def is_prime(num):
    if num == 1:
        return True
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return True
    return False

n, m = map(int, input().split())

for i in range(n, m+1):
    if not is_prime(i):
        print(i)

# Solution
# - (1) 처음에 2~n-1 비교 -> 시간 초과
# - (2) 그래서 2~루트n+1까지 비교 -> 틀림
# - (3) n, m를 포함해야함... -> ok!