S = list(map(str, input()))
strArr = []
intArr = []

for s in S:
  if (s.isdigit()):
    intArr.append(int(s))
  else:
    strArr.append(s)


if (len(intArr)):
  print(''.join(sorted(strArr)) + str(sum(intArr)))
else:
  print(''.join(sorted(strArr)))