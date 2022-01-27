data = list(input())

leftSum = 0
rightSum = 0

for i in range(len(data)//2):
  leftSum += int(data[i])

for i in range(len(data)//2, len(data)):
  rightSum += int(data[i])

if leftSum == rightSum:
  print('LUCKY')
else:
  print('READY')