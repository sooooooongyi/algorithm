import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

direction = [    
    # case 1
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    # case 2
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    # case 3
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [0, 1], [-1, 1], [-2, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    # case 4
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [-1, 1], [-1, 2]],
    [[0, 0], [0, 1], [-1, 1], [1, 0]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    # case 5
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [-1, 1], [0, 1], [1, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]]
  ]

def tetromino(x, y):
  max_value = 0
  for i in range(19):
    sum = 0
    for j in range(4):
      if 0 <= x + direction[i][j][0] < n and 0 <= y + direction[i][j][1] < m:
        sum += graph[x + direction[i][j][0]][y + direction[i][j][1]]
      else:
        break
    max_value = max(max_value, sum)
  return max_value

for i in range(n):
  for j in range(m):
    answer = max(answer, tetromino(i, j))

print(answer)