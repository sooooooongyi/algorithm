import sys
input = sys.stdin.readline

data = list(input())
answer = 0

for i in range(len(data)-1):
    if answer <= 1 or int(data[i]) <= 1:
        answer += int(data[i])
    else:
        answer *= int(data[i])

print(answer)