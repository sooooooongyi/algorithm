go_map = [[0]*19 for i in range(19)]
count = int(input())
for i in range(count):
    x, y = map(int, input().split())
    go_map[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(go_map[i][j], end=" ")
    print()