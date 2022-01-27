data = list(input())
alphabet = []
total = 0

for element in data:
  if element.isalpha():
    alphabet.append(element)
  else:
    total += int(element)

alphabet.sort()
print(''.join(alphabet), total, sep='')