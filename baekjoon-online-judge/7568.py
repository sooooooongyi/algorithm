# 7568 - 덩치
# Solution
# (1) 처음엔 x, y에 대해 sorting을 진행하려고 했음 -> 근데 기존 리스트를 바꾸면 출력 index가 어그러짐 -> 그거 다시 비교해서 짜려면 시간 오래걸림 & 비효율적
# (2) 문제는 "등수" 출력, 즉 나보다 덩치 큰 사람이 몇명인지 check 한뒤 +1만 하면 되는거! 2중 for문으로 해결 -> o

N = int(input())
graph = []

for _ in range(N):
    x, y = input().split()
    graph.append([int(x), int(y)])

for i in range(N):
    count = 0
    x = graph[i][0]
    y = graph[i][1]

    for j in range(N):
        if graph[j][0]>x and graph[j][1]>y:
            count +=1
    print(count+1, end=' ')