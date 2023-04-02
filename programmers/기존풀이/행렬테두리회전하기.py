def solution(rows, columns, queries):
  answer = []
  data = [[0]*columns for _ in range(rows)]
  num = 1

  for i in range(rows):
    for j in range(columns):
      data[i][j] = num
      num += 1

  for x1, y1, x2, y2 in queries:
    start = data[x1 - 1][y1 - 1]
    min_value = start

    for i in range(x1 - 1, x2 -1):
      temp = data[i + 1][y1 - 1]
      data[i][y1 - 1] = temp
      min_value = min(min_value, temp)

    for i in range(y1 - 1, y2 - 1):
      temp = data[x2 - 1][i + 1]
      data[x2 -1][i] = temp
      min_value = min(min_value, temp)

    for i in range(x2 - 1, x1 - 1, -1):
      temp = data[i - 1][y2 -1]
      data[i][y2 - 1] = temp
      min_value = min(min_value, temp)

    for i in range(y2 - 1, y1 - 1, -1):
      temp = data[x1 - 1][i - 1]
      data[x1 - 1][i] = temp
      min_value = min(min_value, temp)

    data[x1 - 1][y1] = start
    answer.append(min_value)

  return answer