# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     bridge = deque([0] * bridge_length)
#     trucks = deque(truck_weights)
#     seconds = 1
#     truck_count = 1
#     bridge_sum = sum(bridge)
    
#     bridge[-1] = truck_weights[0]
#     trucks.popleft()
    
#     while truck_count and not all(i ==0 for i in bridge):
#         bridge_sum -= bridge[0]
#         bridge_sum += bridge[-1]
#         # 시간이 지나, 위치 이동
#         if bridge.popleft() != 0:
#             truck_count -= 1
#         seconds += 1
#         # 다리 위에 못 올라가는 경우
#         if not trucks: 
#             bridge.append(0)
#             continue
#         if truck_count > bridge_length or (bridge_sum + trucks[0]) > weight: 
#             bridge.append(0)
#             continue
#         # 다리 위에 올라가는 경우
#         bridge.append(trucks.popleft())
#         truck_count += 1

#     return seconds

# # print(solution(2, 10, [7, 4, 5, 6]))
# # print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))

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