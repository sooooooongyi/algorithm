def solution(dots):
    diff_width = max([i[0] for i in dots]) - min([i[0] for i in dots])
    diff_height = max([i[1] for i in dots]) - min([i[1] for i in dots])
    return diff_width * diff_height