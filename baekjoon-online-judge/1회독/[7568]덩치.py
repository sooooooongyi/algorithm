# 🌜, ✨ 배열 순회 + sort?

n = int(input())
dataList = []
rankList = []

for _ in range(n):
    x, y = map(int, input().split())
    dataList.append([x, y])
    
for i in range(n):
    cnt = 0 # 나보다 덩치가 큰 사람의 수
    for j in range(n):
        if dataList[i][0] < dataList[j][0] and dataList[i][1] < dataList[j][1]:
            cnt += 1
    rankList.append(cnt+1)
print(*rankList)