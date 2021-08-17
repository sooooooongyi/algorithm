num = int(input())
num_list = [0 for i in range(23)]
call_list = list(map(int, input().split()))

for i in range(len(call_list)):
    num_list[call_list[i]-1] +=1

for i in range(len(num_list)):
    print(num_list[i], end= " ")