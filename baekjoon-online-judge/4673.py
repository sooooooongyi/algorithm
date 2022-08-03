numbers = set(range(1, 10000))
remove_set = set()

for number in numbers:
  for char in str(number):
    number += int(char)
  remove_set.add(number)

result = numbers - remove_set
for self_num in sorted(result):
  print(self_num)