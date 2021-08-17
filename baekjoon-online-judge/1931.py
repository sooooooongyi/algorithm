# 그리디 알고리즘 - 회의실 배정
N = int(input())
list = []
count = 0
endTime = 0

for i in range(N):
    start, end = map(int, input().split())
    list.append([start, end])

list.sort(key = lambda x: (x[1], x[0]))

for i in range(N):
    if endTime <= list[i][0]:
        endTime = list[i][1]
        count += 1

print(count)