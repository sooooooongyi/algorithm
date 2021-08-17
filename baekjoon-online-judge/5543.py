# 수학 - 상근날드
# Solution
# (1) 그냥 문제.. -> o

burger = []
beverage = []

for _ in range(3):
    burger.append(int(input()))

for _ in range(2):
    beverage.append(int(input()))

print(min(burger)+min(beverage)-50)