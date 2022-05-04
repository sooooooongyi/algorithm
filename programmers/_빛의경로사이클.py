def goto(grid, visited, start):
    x, y, d = start
    direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    length = 0

    while True:
        if visited[x][y][d]:
            break

        visited[x][y][d] = True
        length += 1

        if grid[x][y] == 'L':
            d = (d+1)%4
        elif grid[x][y] == 'R':
            d = (d-1)%4

        x = (x + direction[d][0]) % len(grid)
        y = (y + direction[d][1]) % len(grid[0])

    return length

def solution(grid):
    answer = []
    visited = [[[False]*4 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                if visited[i][j][d] == False:
                    answer.append(goto(grid, visited, [i, j, d]))
    answer.sort()
    return answer