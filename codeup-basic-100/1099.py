board = []
for i in range(10):
    board.append(list(map(int, input().split())))

# init : 개미집에서 출발
x = 1
y = 1

while(1) :
    if(board[x][y]==2):
        board[x][y] = 9
        break
    else :
        board[x][y] = 9
    if(y+1 == 9 or board[x][y+1] ==1):
        if(x+1 == 9 and board[x][y+1]==1):
            break
        elif (board[x+1][y] ==2):
            board[x+1][y] = 9
            break
        else :
            x += 1
            board[x][y] = 9
    else :
        if(board[x][y+1] == 2):
            board[x][y+1] = 9
            break
        else :
            y += 1
            board[x][y] = 9

for i in range(10):
    for j in range(10):
        print(board[i][j], end=" ")
    print()