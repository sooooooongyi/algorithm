# 🌜 h % (n+1) 공간에 몇개,  w % (m+1) 공간에 몇개 계산.
# 대신, 마지막 칸은 각각 h % (n+1), w % (m+1) 로 계산해서 더해줘야함
# ✨ h줄 w줄에 대하여 각각 들어갈 수 있는 인원을 서로 곱하기.

import math
import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

cntH = math.ceil(h/(n+1))
cntW = math.ceil(w/(m+1))

print(cntH * cntW)