# 🌜 그냥 시키는대루... 파이썬 배열 사용하기!
# ✨ Set을 이용해야한당.

import sys
input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    commandStr = list(input().split())
    
    if len(commandStr) == 1:
        if commandStr[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else: 
        command, value = commandStr[0], int(commandStr[1])
        
        if command == 'add':
            s.add(value)
        if command == 'remove':
            s.discard(value) 
        if command == 'check':
            if value in s:
                print(1)
            else:
                print(0)       
        if command == 'toggle':
            if value in s:
                s.discard(value)
            else:
                s.add(value)  