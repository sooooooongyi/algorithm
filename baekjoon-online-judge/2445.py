# 구현 - 별찍기8
n = int(input())
for i in range(1, n+1):
    for _ in range(i):
        print('*', end='')
    for _ in range(2*(n-i)):
        print(' ', end='')
    for _ in range(i):
        print('*', end='')
    print()

for i in range(1, n):
    for _ in range(n-i):
        print('*', end='')
    for _ in range(2*i):
        print(' ', end='')
    for _ in range(n-i):
        print('*', end='')
    print()