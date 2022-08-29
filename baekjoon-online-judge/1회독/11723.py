import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
  string = input().split()

  if len(string) == 1:
    if string[0] == 'all':
      S = set([i for i in range(1, 21)])
    else:
      S = set()

  else:
    command, value = string[0], string[1]
    value = int(value)

    if command == 'add':
      S.add(value)
    if command == 'remove':
      S.discard(value)
    if command == 'check':
      if value in S:
        print(1)
      else:
        print(0)
    if command == 'toggle':
      if value in S:
        S.discard(value)
      else:
        S.add(value)