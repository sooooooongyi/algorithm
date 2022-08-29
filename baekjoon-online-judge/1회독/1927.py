import sys
import heapq
input = sys.stdin.readline

N = int(input())
h = [] 

for i in range(N):
    n = int(input())
    if n==0:
        try:
            print(heapq.heappop(h))
        except:
            print(0)
    else:
        heapq.heappush(h, n)