from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    bridge_sum = sum(bridge)

    while bridge:
        answer += 1
        bridge_sum -= bridge[0]
        bridge_sum += bridge[-1]
        bridge.popleft()
        if truck_weights:
            if bridge_sum + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0) 
    return answer