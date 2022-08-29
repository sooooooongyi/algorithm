# 구간 합 - binary index tree로 해결

# Solution
# (1) 기존 dp 방식처럼 미리 prefix 배열에 구간합을 넣어놓고 업데이트 마다 2차원 배열 갱신 -> 시간초과

'''
def modify_prefix(arr, p, b, c):
    arr[b-1] = c
    del p[1:len(p)]
    get_prefix(arr, p)

def get_prefix(arr, p):
    sum = 0
    for i in arr:
        sum += i
        p.append(sum)

N, M, K = map(int, input().split())
p = [0]
arr = []
result = []

# 숫자 입력
for i in range(N):
    num = int(input())
    arr.append(num)

# a=1 or a=2인 상황
for i in range(M+K):
    a, b, c = map(int, input().split())
    if a==1:
        modify_prefix(arr, p, b, c)
    else:
        result.append(p[c]-p[b-1])

for i in result:
    print(i)

'''

import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())

arr = [0]*(n+1)
tree = [0]*(n+1)

def prefix_sum(i):
    result = 0
    while i>0:
        result += tree[i]
        i -= (i&-i)
    return result
    
def update(i, dif):
    while i<=n:
        tree[i] += dif
        i += (i&-i)

def interval_sum(start, end):
    return prefix_sum(end)-prefix_sum(start-1)

for i in range(1, n+1):
    x = int(input())
    arr[i] =x
    update(i, x)

for i in range(m+k):
    a, b, c = map(int, input().split())
    if a==1:
        update(b, c - arr[b])
        arr[b] = c
    else:
        print(interval_sum(b, c))