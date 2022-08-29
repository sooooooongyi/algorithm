# 이진 탐색 - 수 찾기
# Solution
# (1) mid값을 절반으로 나눠 탐색을 절반으로 범위를 좁혀서 주어진 값을 찾는다. -> O

def BSearch(target):
    first = 0
    last = N-1

    while first <= last:
        mid = (first+last)//2
        if arr[mid] == target:
            print(1)
            return
        else:
            if arr[mid] <= target:
                first = mid+1
            else:
                last = mid-1
    print(0)
    return

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
check = list(map(int, input().split()))

for i in range(M):
    BSearch(check[i])