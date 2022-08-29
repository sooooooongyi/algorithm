import sys
input = sys.stdin.readline

A, B = map(str, input().split())

newA = ''
newB = ''

for element in A:
  if element == '6':
    newA += '5'
  else:
    newA += element

for element in B:
  if element == '6':
    newB += '5'
  else:
    newB += element

print(int(newA)+int(newB))

newA = ''
newB = ''

for element in A:
  if element == '5':
    newA += '6'
  else:
    newA += element

for element in B:
  if element == '5':
    newB += '6'
  else:
    newB += element

print(int(newA)+int(newB), end=" ")

# 클린코드
A, B = input().split()
min_num = int(A.replace('6', '5')) + int(B.replace('6','5'))
max_num = int(A.replace('5', '6')) + int(B.replace('5','6'))