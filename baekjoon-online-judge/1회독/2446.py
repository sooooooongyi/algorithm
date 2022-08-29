# 구현 - 별찍기-9
# Solution
# (1) 2*n-1 2*n+1 노가다 -> o

n = int(input())

for i in range(n):
    for j in range(i):
        print(' ', end='')
    for k in range(2*n-1-2*i):
        print('*', end='')
    print()

for i in range(1, n):
    for j in range(n-i-1):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()