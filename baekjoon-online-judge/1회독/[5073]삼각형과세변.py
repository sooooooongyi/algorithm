# 🌜, ✨ 그냥 계속 구하기...

# numberList = list(map(int, input().split()))
# print(numberList)

while True:
    numberList = list(map(int, input().split()))
    numberList.sort(reverse=True)

    a, b, c = numberList[0], numberList[1], numberList[2]
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if numberList[0] >= numberList[1] + numberList[2]:
        print('Invalid')
        continue
    
    if a == b and b == c and a == c:
        print('Equilateral')
        continue
        
    if a == b or a == c or b == c:
        print('Isosceles')
        continue
        
    if a != b != c:
        print('Scalene')
        continue