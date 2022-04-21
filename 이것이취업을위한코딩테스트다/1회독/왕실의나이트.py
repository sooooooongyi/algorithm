MIN_LIMIT = 1
MAX_LIMIT = 8

input_data = input()
row = int(input_data[1])
# zero base x 1부터 시작하기 때문에 +1
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= MIN_LIMIT and next_row <= MAX_LIMIT and next_column >= MIN_LIMIT and next_column <= MAX_LIMIT:
        result += 1

print(result)