# 이진 탐색 - 나무 자르기
# Solution
# (1) mid의 값이 그냥 인덱스가 아닌데, 인덱스로 처리해서 start와 end가 꼬임 -> o
# (2) 알고보면 그냥 전형적인 이진 탐색 문제

N, M = map(int, input().split())
size = list(map(int, input().split()))

def BSearch(start, end, size):
    while start <= end:
        mid = (start+end)//2
        result = get_length(mid, size)
        if result >= M:
            start = mid+1
        else:
            end = mid-1
    return end

def get_length(mid, size):
    result = 0
    for i in range(N):
        if size[i] > mid:
            result += size[i]-mid
    return result

print(BSearch(1, max(size), size))