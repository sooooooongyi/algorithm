words = input()

answer = ''
isTag = False
stack = []

for word in words:
  if word == '<':
    answer += ''.join(stack[::-1])
    stack = []
    isTag = True
    stack.append(word)
  elif word == '>':
    isTag = False
    answer += ''.join(stack) + word
    stack = []
  elif word == ' ':
    if isTag == False:
      answer += ''.join(stack[::-1]) + word
      stack = []
    else:
      stack.append(word)
  else:
    if isTag == True:
      stack.append(word)
    else:
      stack.append(word)

answer += ''.join(stack[::-1])
print(answer)