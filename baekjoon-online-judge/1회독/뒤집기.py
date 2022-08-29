import sys
input = sys.stdin.readline

S = list(input())

zero_num = 0
one_num = 0

for i in range(1, len(S)):
  if S[i-1] == '1' and S[i] == '0':
    one_num += 1
  elif S[i-1] == '0' and S[i] == '1':
    zero_num += 1

print(max(zero_num, one_num))