# 구현 - 2007년
date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
days = 0

for i in range(x):
    days += date[i]

days += y
days %= 7

if days == 1:
    print("MON")
elif days == 2:
    print("TUE")
elif days == 3:
    print("WED")
elif days == 4:
    print("THU")
elif days == 5:
    print("FRI")
elif days == 6:
    print("SAT")
else:
    print("SUN")