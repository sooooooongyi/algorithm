def solution(lines):
    graph = [0] * 200
    answer = 0
    for line in lines:
        x, y = line[0], line[1]
        for i in range(x, y):
            graph[i] += 1
    return 200 - graph.count(0) - graph.count(1)