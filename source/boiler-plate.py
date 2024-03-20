import sys
from collections import deque
from itertools import combinations

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
nData= [list(map(int, input().split())) for _ in range(N)]