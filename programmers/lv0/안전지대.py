def solution(board):
    n = len(board[0])
    answer = 0
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                continue
            if board[i][j] == 1:
                for direction in directions:
                    ni, nj = direction[0] + i , direction[1] + j
                    if ni >= 0 and ni < n and nj >= 0 and nj < n and board[ni][nj] != 1:
                        board[ni][nj] = 2
    for i in board:
        answer += i.count(0)
    return answer
