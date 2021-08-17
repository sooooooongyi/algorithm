# [그리디] 거스름돈 p.87

coins = [500, 100, 50, 10]
money = 1260
count = 0

for coin in coins:
    count += money//coin
    money %= coin

print(count)