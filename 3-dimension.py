arr = [[[1,2,3], [4,5,6], [7,8,9]],[[0,0,0], [0,0,0], [0,0,0]]]
print(arr[0][1])

for h in range(2):
  for y in range(3):
    for x in range(3):
      print(h, y, x, arr[h][y][x])
