# 🌜 작은 단위로 쪼개 생각하기
# ✨ 문제 잘 이해하기, 대칭을 양쪽에서 벌어지는 num - i, num + i 으로 표현!

def changeSwitch(num):
    if switchs[num] == 0:
        switchs[num] = 1
    else:
        switchs[num] = 0

n = int(input())
switchs = [-1] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    sex, num = map(int, input().split())
    
    if sex == 1:
        for i in range(num, n+1, num):
            changeSwitch(i)
    if sex == 2:
        changeSwitch(num)
        for i in range(n//2):
            if num + i > n or num - i < 1:
                break
            if switchs[num + i] == switchs[num - i]:
                changeSwitch(num+i)
                changeSwitch(num-i)
            else:
                break
            
for i in range(1, n+1):
    print(switchs[i], end= " ")
    if i % 20 == 0:
        print()