# 냅색 알고리즘 (0-1 배낭문제) -평범한 배낭
# Solution
# (1) K를 담을 수 있는 배낭에 무게 w 가치 v 가진 여러 물건들을 넣을 수 있는데, 이중 가장 높은 v를 가지게끔 하는 값이 무엇인가 구하는 문제
# N+1XK+1 배열을 만든 후 2중 for문을 도는데, 이때 j값이 배낭속 넣을 수 있는 무게라고 설정
# 예를 들어 i=1 w가 5라면 j가 5가 될때까진 배낭에 담을 수 없음!
# 만약 j값이 충분히 커져 담을 수 있다면, max함수로 1) 현재물건가치+현재물건을 담고 남은 공간의 가치 2) 담지않았을때 이미 j무게만큼 확보한 가치 중에 큰 값을 저장
# 이걸 [N][K] 행까지 반복하면 해당 K 무게에 대한 최대 가치를 찾을 수 있음!

N, K = map(int, input().split())
arr = [[0, 0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    w, k = map(int, input().split())
    arr.append([w, k])

for i in range(1, N+1):
    for j in range(1, K+1):
        w = arr[i][0]
        v = arr[i][1] 
        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v+knapsack[i-1][j-w], knapsack[i-1][j])
print(knapsack[N][K])