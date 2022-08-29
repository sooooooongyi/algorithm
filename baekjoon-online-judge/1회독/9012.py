T = int(input())

for _ in range(T):
    sum = 0
    string = list(input())
    for ch in string:
        if ch=='(':
            sum += 1
        else:
            sum -= 1     
        if sum < 0:
            # print('NO')
            break;
    if sum==0:
        print('YES')
    else:
        print('NO')