t = int(input())
list = []
for i in range(t):
    list.append(int(input()))
list.sort()
for i in range(t):
    print(list[i])