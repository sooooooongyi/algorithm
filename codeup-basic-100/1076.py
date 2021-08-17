num = ord(input())
start = 97
while(1):
    print(chr(start), end=' ')
    start += 1
    if(start==num+1):
        break