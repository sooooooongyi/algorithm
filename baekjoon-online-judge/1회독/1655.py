# 우선순위 큐 - 가운데를 말해요
# Solution
# (1) 흔히 생각할 수 있는 n^2로 문제 풀이 -> 시간 초과
# (2) 이분탐색 bisect 모듈을 이용한 문제 풀이 -> 시간 초과 (왜 시간 초과인가..)
# (3) 최대 힙과 최소 힙을 이용한 문제 풀이 -> o (이해하는데 내 머리 시간 초과^^)
# 또 까먹고 다시 하려면 너무 억울할꺼같아서, 문제 풀이 방향을 적어둔다.

import sys
import heapq

n = int(sys.stdin.readline())
max_h, min_h = [], []

for _ in range(n):
    num = int(sys.stdin.readline())
    # 중간값) 최대힙과 최소힙을 원소들을 "절반"으로 나누기 위해, 사용한다.
    # 최소힙 - 원소 튜플중 [0]이 작을 수록 우선
    # 최대힙 - 원수 튜플중 [0]이 클수록 우선 (파이썬은 최소힙을 제공. 음수 이용해야함)
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, (-num, num))
    else:
        heapq.heappush(min_h, (num, num))
    # 만약 절반 이후의 값(최소힙)의 최소값이 절반 이전의 값(최대힙)의 최댓값보다 작으면 값을 서로 바꿔줌(그래야 정렬된 상태에서의 중간값을 찾을 수있음) 
    if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0][1] > min_h[0][1]:
        max_value = heapq.heappop(max_h)[1]
        min_value = heapq.heappop(min_h)[1]
        heapq.heappush(max_h, (-min_value, min_value))
        heapq.heappush(min_h, (max_value, max_value))
    # n번 반복 후엔 max_h 과 min_h으로 절반 나뉜 두가지 힙 존재
    # 이 중, max_h의 가장 작은 값(사실 가장 큰값)이 중간값
    print(max_h[0][1])