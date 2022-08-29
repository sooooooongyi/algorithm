A, B = map(int, input().split())
total = 1

while True:
  if A == B:
    break
  elif (B % 2 != 0 and B % 10 != 1) or B < A:
    total = -1
    break
  else:
    if B % 10 == 1:
      B //= 10
      total += 1
    else:
      B //= 2
      total += 1
print(total)