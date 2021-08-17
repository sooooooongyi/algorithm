# [구현] 왕실의 나이트

# 내 코드
# 해설 코드와 마지막 체크판에서 나갔는지 아닌지에 대한 조건만 다름!
# 파이썬 ord 함수 공부필요★

position = input()

count = 0
x = int(position[1])
y = int(ord(position[0]))- int(ord('a')) + 1

types = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

for type in types:
    nx = x+type[0]
    ny = y+type[1]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    count +=1 

print(count)