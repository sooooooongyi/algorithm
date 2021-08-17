numX, numY = map(int, input().split())
board = [
    [0 for i in range(numY)]
    for j in range(numX)
]

num = int(input())
for i in range(num):
    l, d, x, y = map(int, input().split())
    if(d == 0):
        for i in range(y-1, y+l-1):
            board[x-1][i] = 1
    else :
        for i in range(x-1, x+l-1):
            board[i][y-1] = 1

for i in range(numX):
    for j in range(numY):
        print(board[i][j], end=" ")
    print()