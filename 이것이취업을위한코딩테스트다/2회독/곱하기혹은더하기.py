arr = input()
result = 0

for i in range(1, len(arr)):
  if arr[i-1] == '0':
    result += int(arr[i])
  else:
    result *= int(arr[i])

print(result)