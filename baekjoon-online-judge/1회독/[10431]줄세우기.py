# 🌜, ✨ 리스트 순회하며, 나보다 큰 숫자들 계속 더하기.

p = int(input())
answer = 0

for _ in range(p):
    answer = 0
    arrList = list(map(int, input().split()))
    arrTest = []
    
    for i in arrList:
        arrTest.append(i)
        arrTest.sort()
        answer += len(arrTest) - (arrTest.index(i) + 1)
        
    print(p+1, answer)