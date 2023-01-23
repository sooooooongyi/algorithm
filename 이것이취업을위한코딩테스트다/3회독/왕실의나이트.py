# [구현] 난이도1

data = input()
row = int(data[1])
column = int(ord(data[0]) - ord('a')) + 1
answer = 0

steps = [(-2, 1), (-2, -1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if 1 <= next_row <= 8 and 1 <= next_column <= 8:
    answer += 1

print(answer)