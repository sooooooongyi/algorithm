# 그리디 알고리즘 - 주유소
N = int(input())
cost_list = list(map(int, input().split()))
price_list = list(map(int, input().split()))
cost = 0

min = price_list[0]
cost += cost_list[0]*min

for i in range(1, N-1):
    if min > price_list[i]:
        min = price_list[i]
    cost += cost_list[i]*min
    
print(cost)