N = int(input())
list = list(map(int, input().split()))
sum = 0

def is_prime(num):
    if num == 1:
        return True
    for i in range(2, num):
        if num%i == 0:
            return True
    return False


for i in range(N):
    if not is_prime(list[i]):
        sum += 1
            
print(sum)