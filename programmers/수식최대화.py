from itertools import permutations
from selectors import EpollSelector

def operation(op1, op2, operator):
  if operator=='*':
    return str(int(op1) * int(op2))
  if operator=='+':
    return str(int(op1) + int(op2))
  if operator=='-':
    return str(int(op1) - int(op2))

def calculate(expression, operator):
  array = []
  temp = ''

  for char in expression:
    if char.isdigit()==True:
      temp += char
    else:
      array.append(temp)
      array.append(char)
      temp = ''
    
  array.append(temp)

  for op in operator:
    stack = []
    while len(array):
      item = array.pop(0)
      if item == op:
        stack.append(operation(stack.pop(), array.pop(0), op))
      else:
        stack.append(item)
    array = stack
  return abs(int(array[0])) 

def solution(expression):
  op = ['*', '-', '+']
  op_permutations = list(permutations(op, 3))
  result = []

  for operator in op_permutations:
    result.append(calculate(expression, operator))

  return max(result)