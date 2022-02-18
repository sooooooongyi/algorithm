def solution(bridge_length, weight, truck_weights):
  answer = 0
  load = [0]*bridge_length

  while len(load):
    answer += 1
    load.pop(0)

    if truck_weights:
      if sum(load) + truck_weights[0] <= weight:
        load.append(truck_weights.pop(0))
      else:
        load.append(0)

  return answer

print(solution(2, 10, [7, 4, 5, 6]))