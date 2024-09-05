# 🌜, ✨ 2차원 배열 돌기?

n = int(input())
graph = []

for _ in range(n):
    row = list(input())
    graph.append(row)
    
# head search
heartX = 0
heartY = 0
isFindHead = False
for i in range(n):
    for j in range(n):
        if graph[i][j] == '*':
            heartX = i+1
            heartY = j
            isFindHead = True
            break
    if isFindHead == True:
        break
        
# left hand search
body = []
cnt = 0
for i in range(heartY-1, -1, -1):
    if graph[heartX][i] == '*':
        cnt += 1
    else:
        break
body.append(cnt)

# right hand search
cnt = 0
for i in range(heartY+1, n, 1):
    if graph[heartX][i] == '*':
        cnt += 1
    else: 
        break
body.append(cnt)

#body search
bodyX = 0
bodyY = heartY
cnt = 0
for i in range(heartX+1, n, 1):
    if graph[i][heartY] == '*':
        cnt += 1
    else:
        bodyX = i-1
        break
body.append(cnt)

# left leg search
cnt = 0
for i in range(bodyX+1, n, 1):
    if graph[i][bodyY-1] == '*':
        cnt += 1
    else:
        break
body.append(cnt)

# right leg search
cnt = 0
for i in range(bodyX+1, n, 1):
    if graph[i][bodyY+1] == '*':
        cnt += 1
    else:
        break
body.append(cnt)

print(heartX+1, heartY+1)
print(' '.join(map(str, body)))