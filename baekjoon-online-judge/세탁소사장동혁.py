T = int(input())

for _ in range(T):
  data = int(input())
  quater = data // 25
  data %= 25

  dime = data // 10
  data %= 10

  nickel = data // 5
  data %= 5

  penny = data // 1

  print(quater, dime, nickel, end=" ")
  print(penny)