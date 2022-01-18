import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque()
answer = []

for i in range(1, N+1):
  queue.append(i)

while queue:
  for _ in range(K-1):
    queue.append(queue.popleft())
  answer.append(queue.popleft())

print('<', end='')
for i in range(len(answer)-1):
  print('%d, ' %answer[i], end='')
print('%d' %answer[-1], end='')
print('>')