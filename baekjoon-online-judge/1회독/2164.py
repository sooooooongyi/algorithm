import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque([i for i in range(1, n+1)])

while (len(q)>1):
  q.popleft()
  result = q.popleft()
  q.append(result)

print(q[0])