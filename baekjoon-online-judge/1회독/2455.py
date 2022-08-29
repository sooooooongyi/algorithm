import sys
input = sys.stdin.readline

STATION_NUMBER = 4

data = [0] * STATION_NUMBER
out_number, in_number = map(int, input().split())
data[0] = in_number

for i in range(1, STATION_NUMBER):
  out_number, in_number = map(int, input().split())
  data[i] = data[i-1] + in_number - out_number

print(max(data))