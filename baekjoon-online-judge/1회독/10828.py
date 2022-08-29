# 자료구조 - 스택
# Solution
# (1) n = int(input())으로 구현했더니 시간 초과 -> x
# (2) sys을 import하고 sys.stdin.readline을 사용 -> o

import sys

stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        stack.append(cmd[1])

    elif cmd[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    elif cmd[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

    elif cmd[0] == 'size':
        print(len(stack))

    elif cmd[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)