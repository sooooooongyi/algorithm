N = int(input())
cnt = 0

for _ in range(N):
  alphabets= []
  words = input()

  for i, word in enumerate(words):
    if word not in alphabets:
      alphabets.append(word)
    else:
      if alphabets[-1] == word:
        continue
      else:
        cnt += 1
        break

print(N-cnt)