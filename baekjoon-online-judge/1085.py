# 수학 - 직사각형 탈출
# Solution
# (1) 경계로부터 차이가 작은것 -> x
# (2) 경게가 w,h도 있지만 0,0도 해당 -> o

x, y, w, h = map(int, input().split())
print(min(w-x, h-y, x, y))