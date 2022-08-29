import sys
import math
input = sys.stdin.readline

S = int(input())

print(math.floor((-1 + (1 + 8*S)**(1/2))/2))