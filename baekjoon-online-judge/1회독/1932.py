# DP - 정수 삼각형
# Solution
# (1) 도무지 공식을 모르겠음... 
# (2) 그냥 생각했던 그 공식 (위에서 큰걸 선택하면서 내려옴)을 그대로 구현하면 되는 문제. (대신 모든 케이스 다 따짐) -> o

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

k = 2
for i in range(1, n):
    for j in range(k):
        if j==0:
            arr[i][j] = arr[i-1][j] + arr[i][j]
        elif j==i:
            arr[i][j] = arr[i-1][j-1] + arr[i][j]
        else:
            arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + arr[i][j]
    k +=1

print(max(arr[n-1]))