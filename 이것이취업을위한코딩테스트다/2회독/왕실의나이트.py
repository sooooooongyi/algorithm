data = input()
x = int(data[1])
y = int(ord(data[0])) - int(ord('a')) 
answer = 0

d = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

for dx, dy in d:
  nx = x + dx
  ny = y + dy
  if nx < 1 or ny < 1 or nx > 9 or ny > 9:
    continue
  answer += 1

print(answer)