num = int(input())
num_list = list(map(int, input().split()))
for i in range(num):
    print(num_list[num-i-1], end=" ")