# 현재 상태에서 회전하거나 회전하지않거나!! (연쇄적으로 돌아제끼는건 무시)

import sys
from collections import deque
input = sys.stdin.readline


def check_right(gear, d):
    if gear > 4 or gears[gear-1][2] == gears[gear][6]:
        return

    if gears[gear-1][2] != gears[gear][6]:
        check_right(gear + 1, -d)
        gears[gear].rotate(d)


def check_left(gear, d):
    if gear < 1 or gears[gear][2] == gears[gear+1][6]:
        return

    if gears[gear][2] != gears[gear+1][6]:
        check_left(gear - 1, -d)
        gears[gear].rotate(d)


gears = {}
for i in range(1, 5):
    gears[i] = deque(
        list(map(int, list(sys.stdin.readline().replace('\n', '')))))
n = int(input())

for _ in range(n):
    gear, d = map(int, input().split())
    check_right(gear + 1, -d)
    check_left(gear - 1, -d)

    gears[gear].rotate(d)

answer = 0
for i in range(4):
    answer += (2**i) * gears[i+1][0]

print(answer)
