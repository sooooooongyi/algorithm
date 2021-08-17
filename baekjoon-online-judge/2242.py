# 구현 - 별찍기-5
# Solution
# (1) o

n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()