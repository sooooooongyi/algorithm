# 이진 탐색 - 숫자 카드
# Solution
# (1) 그냥 이진 탐색 문제 -> o

N = int(input())
n_list = list(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def BSearch(start, end, target, list):
    while start <= end:
        mid = (start+end)//2
        if list[mid] == target:
            return True
        if list[mid] >= target:
            end = mid-1
        else:
            start = mid+1
    return False

for i in m_list:
    if BSearch(0, len(n_list)-1, i, n_list):
        print(1, end=' ')
    else:
        print(0, end=' ')