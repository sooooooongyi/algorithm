alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
cnt = len(word)

for i in range(len(alphabet)):
  cnt -= word.count(alphabet[i])

print(cnt)