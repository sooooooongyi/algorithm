num = int(input())
list = []
for i in range(num):
    list.append(int(input()))

list = sorted(list, reverse=True)

for i in list:
    print(i, end=' ')