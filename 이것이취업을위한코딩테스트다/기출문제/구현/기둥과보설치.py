def isSafe(answer):
    for x, y, frame in answer:
        if frame == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif frame == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, frame, operation = build
        if operation == 1:
            answer.append([x, y, frame])
            if not isSafe(answer): 
                answer.remove([x, y, frame])
        elif operation == 0:
            answer.remove([x, y, frame])
            if not isSafe(answer): 
                answer.append([x, y, frame])
    
    answer.sort()
    return answer