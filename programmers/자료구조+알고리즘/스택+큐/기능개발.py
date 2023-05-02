from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    days = deque()
    for i in range(len(speeds)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
        
    init = days.popleft()
    count = 1
    
    while days:
        if days[0] <= init:
            days.popleft()
            count += 1
        else:
            init = days.popleft()
            answer.append(count)
            count = 1
    answer.append(count)
    return answer