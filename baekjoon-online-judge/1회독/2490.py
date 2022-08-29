# 구현 - 윷놀이
# Solution
# (1) 파이썬에는 switch문이 없기에 if로 처리

for _ in range(3):
    arr = list(map(int, input().split()))
    count = sum(arr)
    if count==0:
        print('D')
    elif count==1:
        print('C')
    elif count==2:
        print('B')
    elif count==3:
        print('A')
    else:
        print('E')