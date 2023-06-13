N = int(input())
data = list(map(int, input().split()))

target = 1
data.sort()

for i in data:
    if i <= target:
        target += i
    else:
      break

print(target)