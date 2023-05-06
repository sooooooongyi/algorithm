from collections import deque

def solution(priorities, location):
    locations = deque([0 for _ in range(len(priorities))])
    locations[location] = 1
    deque_priorities = deque(priorities)
    answer = 0
    
    while True:
        if max(deque_priorities) == deque_priorities[0]:
            answer += 1
            if locations[0] == 1:
                break
            locations.popleft()
            deque_priorities.popleft()
            
        else:
            locations.append(locations.popleft())
            deque_priorities.append(deque_priorities.popleft())
    return answer

print(solution([2, 1, 3, 2], 2))