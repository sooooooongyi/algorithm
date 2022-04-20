def solution(dartResult):
  number  = ''
  numbers = []
  for i in dartResult:
    if i.isdigit():
      number += i
    elif i == 'S':
      number = int(number) ** 1
      numbers.append(number)
      number = ''
    elif i == 'D':
      number = int(number) ** 2
      numbers.append(number)
      number = ''
    elif i == 'T':
      number = int(number) ** 3
      numbers.append(number)
      number = ''
    elif i == '*':
      if len(numbers) > 1:
        numbers[-2] = numbers[-2] * 2
        numbers[-1] = numbers[-1] * 2
      else:
        numbers[-1] = numbers[-1] * 2
    elif i == '#':
      numbers[-1] = numbers[-1] * -1
    
  return sum(numbers)

