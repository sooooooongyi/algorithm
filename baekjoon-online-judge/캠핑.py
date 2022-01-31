index = 1
total = 0

while(True):
  L, P, V = map(int, input().split())
  if not (L == 0 and P == 0 and V == 0):
    total += V//P*L
    total += min(V%P, L)

    print("Case %d: %d" %(index, total))
    index += 1
    total = 0
  else:
    break
