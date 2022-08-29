# 구현 - 직사각형 점 구하기

x_arr = []
y_arr = []

x_result = 0
y_result = 0

for _ in range(3):
    a, b = map(int, input().split())
    x_arr.append(a)
    y_arr.append(b)

for i in range(3):
    if x_arr.count(x_arr[i])%2:
        x_result = x_arr[i]
    if y_arr.count(y_arr[i])%2:
        y_result = y_arr[i]

print(str(x_result)+' '+str(y_result))