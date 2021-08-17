# 구현 - 방 번호

n = input()
arr = [0 for i in range(10)]

for i in n:
    if int(i)==6:
        if arr[6] > arr[9]:
            arr[9] += 1
        else:
            arr[6] += 1
    elif int(i)==9:
        if arr[9] > arr[6]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[int(i)] += 1

print(max(arr))