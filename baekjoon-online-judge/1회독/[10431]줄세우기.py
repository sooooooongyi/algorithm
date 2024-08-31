# 🌜, ✨ 입력된 리스트를 순회하며, 나보다 큰 학생들(한 칸씩 밀릴 학생) 수 구하기

p = int(input())
answer = 0

for i in range(p):
    answer = 0
    arrList = list(map(int, input().split()))[1:]
    arrTest = []
    
    for j in arrList:
        arrTest.append(j)
        arrTest.sort()
        answer += len(arrTest) - (arrTest.index(j) + 1)
        
    print(i+1, answer)