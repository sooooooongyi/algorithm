# 구현 - 열 개씩 끊어 출력하기
# Solution
# (1) i=0인 상황에서는 10으로 나눈 나머지가 0이기때문에, 첫줄에 계행이 됨 -> x
# (2) i!=0인 조건 추가 -> o

string = input()
for i in range(len(string)):
    if i!=0 and i%10==0:
        print()
    print(string[i], end='')