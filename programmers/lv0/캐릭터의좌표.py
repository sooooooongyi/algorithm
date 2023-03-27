def solution(keyinput, board):
    point = [0, 0]
    dic = {'up': 0, 'down': 1, 'left': 2, 'right': 3}
    inputs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    for i in keyinput:
        point[0] += inputs[dic[i]][0]
        point[1] += inputs[dic[i]][1]
        
        if point[0] > board[0] // 2:
            point[0] = board[0] // 2
        if point[0] < (-1) * (board[0] // 2):
            point[0] = (-1) * (board[0] // 2)
            
        if point[1] > board[1] // 2:
            point[1] = board[1] // 2
        if point[1] < (-1) * (board[1] // 2):
            point[1] = (-1) * (board[1] // 2)
    return point