arr = input()
zero_group = 0
one_group = 0

if arr[0] == '0':
  zero_group += 1
else:
  one_group += 1

for i in range(len(arr)-1):
  if arr[i] == '0' and arr[i+1] == '1':
    one_group += 1
  elif arr[i] == '1' and arr[i+1] == '0':
    zero_group += 1

print(max(zero_group, one_group))