# [구현] 상하좌우

# 해설 코드
N = int(input())
move_items = input().split()
move_menu = ['U', 'D', 'L', 'R']
x, y = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for item in move_items:
    for i in range(len(move_menu)):
        if move_menu[i]==item:
            nx = x+dx[i]
            ny = y+dy[i]
        if nx < 1 or nx > N or ny < 1 or ny > N:
            continue
        x, y = nx, ny

print(x, y)