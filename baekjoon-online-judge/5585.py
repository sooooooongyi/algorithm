# 그리디 알고리즘 - 거스름돈
coin = [500, 100, 50, 10, 5, 1]
money = int(input())
money = 1000 - money
sum = 0

for i in range(len(coin)):
    sum += money//coin[i]
    money %= coin[i]
print(sum)