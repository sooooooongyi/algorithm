alphabet = [0] * 26
string = input()

for i in string:
  alphabet[ord(i)-97] += 1

for i in alphabet:
  print(i, end=' ')