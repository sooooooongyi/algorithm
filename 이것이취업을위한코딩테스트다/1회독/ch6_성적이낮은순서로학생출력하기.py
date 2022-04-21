num = int(input())
array = []

for i in range(num):
    info = input().split()
    array.append((info[0], info[1]))

array = sorted(array, key= lambda array : array[1])
for i in array:
    print(array[0], end = ' ')