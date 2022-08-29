def is_prime(num):
    if num == 1:
        return True
    for i in range(2, num):
        if num%i == 0:
            return True
    return False

N = int(input())
M = int(input())
sum = 0
min = 1e9

for i in range(N, M+1):
    if not is_prime(i):
        sum += i
        if i < min:
            min = i

if sum == 0:
    print(-1)
else:
    print("%d\n%d" %(sum, min))