'''
<Idea>
n까지 숫자를 만들 수 있다면 -> n+1을 만들 수 있는지만 확인하면 된다!
(1 ~ n-1)는 조합해서 만들 수 있다.
'''

import sys
input = sys.stdin.readline

N = map(int, input().split())
data = list(map(int, input().split()))

target = 1

for element in data:
    if target < element: # 다음 target 만들 수 있어?
        break
    target += element # 그럼 다음 target 만들어!

print(target)