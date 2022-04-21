import sys
input = sys.stdin.readline

data = list(input())

group = {
    '0': 0,
    '1': 0
}

prev = '0'
for element in data:
    if element != prev:
       group[prev] += 1

    prev = element

print(min(group.values()))