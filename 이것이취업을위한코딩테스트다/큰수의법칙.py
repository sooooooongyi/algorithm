# 가장 큰 수 k개 + 두번째로 큰 수 1개 <- 이 패턴이 반복되는 구조
# (k+1)개의 숫자 수열이 반복되기 때문에 이를 이용한다.

n, m, k = map(int, input().split())
dataArr = list(map(int, input().split()))
result = 0

dataArr.sort()
first = dataArr[n-1]
second =dataArr[n-2]

count = int(m/(k + 1))*k + m%(k+1)
result = count*first + (m-count)*second

print(result)