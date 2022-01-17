import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
data = []

for _ in range(N):
	data.append(int(input()))

data.sort()

# 평균
print(round(sum(data)/N))

# 중앙값
print(data[N//2])

# 최빈값
cnt_data = Counter(data).most_common()
if len(cnt_data) > 1 and cnt_data[0][1]==cnt_data[1][1]:
    print(cnt_data[1][0])
else:
    print(cnt_data[0][0])

# 범위			
print(max(data)-min(data))