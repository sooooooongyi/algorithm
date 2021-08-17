# n이 소수면 true, 아니면 false return
from math import sqrt

while(1):
    count = 0
    n = int(input())
    if n==0:
        break

    for i in range(n+1, 2*n+1):
        if i==1:
            continue 
        elif i==2:
            continue
        else:
            for j in range(2, int(sqrt(i)+1)):
                if i%j==0:
                    break
            else:
                count += 1      
    print(count)