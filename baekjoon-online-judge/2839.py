#그리디 알고리즘 - 설탕 배달

sugar = int(input())
n = 0

while sugar >= 0:
    if sugar%5 ==0:
        n += sugar//5
        sugar %= 5
        break
    sugar -= 3
    n += 1

if sugar != 0:
    print(-1)
else: 
    print(n)