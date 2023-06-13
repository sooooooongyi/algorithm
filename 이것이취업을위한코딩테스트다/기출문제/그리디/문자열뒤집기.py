data = list(input())

zeroCnt = 0
oneCnt = 0

current = -1

for i in data:
    if current == -1:
        current = i
    if i == '1':
        if current == '1':
            continue
        else:
            oneCnt += 1
            current = '1'
    if i == '0':
        if current == '0':
            continue
        else:
            zeroCnt += 1
            current = '0'    
            
print(min(zeroCnt, oneCnt))