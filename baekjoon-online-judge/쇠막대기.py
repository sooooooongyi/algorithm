data = input().replace('()', '0')
stick = 0
cut_stick = 0

for element in data:
  if element == '(':
    stick += 1
    cut_stick += 1
  elif element == '0':
    cut_stick += stick
  else:
    # 잘릴 쇠의 길이가 끝났다.
    stick -= 1

print(cut_stick)