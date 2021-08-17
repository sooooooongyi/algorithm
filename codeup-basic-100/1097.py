board = [
    [0 for i in range(20)]
    for j in range(20)
]

# 바둑판 input
for i in range(0, 19):
    num = input().split()
    board[i] = list(map(int, num))
    #print()

# 반복
repeat = int(input())

for i in range(0, repeat):
    temp = input().split()
    point = list(map(int, temp))
    x = point[0]-1
    y = point[1]-1

    # width
    for j in range(0, 19):
        if board[x][j] == 0:
            board[x][j] = 1
        else:
            board[x][j] = 0

    # cols
    for k in range(0, 19):
        if board[k][y] == 0:
            board[k][y] = 1
        else:
            board[k][y] = 0

# 바둑판 output
for i in range(0, 19):
    for j in range(0, 19):
        print(board[i][j], end=' ')
    print()