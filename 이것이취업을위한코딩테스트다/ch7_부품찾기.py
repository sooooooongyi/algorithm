item = int(input())
item_list = list(map(int, input().split()))

search = int(input())
search_list = list(map(int, input().split()))

# 이진 탐색
def binary_search(item_list, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if item_list[mid] < target:
            start = mid+1
            continue
        if item_list[mid] > target:
            end = mid-1
            continue
        if item_list[mid] == target:
            return True
    return False
    
for i in search_list:
    if binary_search(item_list, i, 0, item-1):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

# 계수 정렬
array = [0] * 1000001
for i in item_list:
    array[i] += 1

for i in search_list:
    if array[i]:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')