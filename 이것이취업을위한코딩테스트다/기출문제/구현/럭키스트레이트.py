array = list(map(int, input()))
prevList = array[0:len(array)//2]
nextList = array[len(array)//2:]

if(sum(prevList) == sum(nextList)):
  print('LUCKY')
else:
  print('READY')