a, b, c = map(int, input().split())
i = 1
while(1):
    if((i%a != 0)or(i%b != 0)or(i%c != 0)):
        i += 1
    else :
        print(i)
        break