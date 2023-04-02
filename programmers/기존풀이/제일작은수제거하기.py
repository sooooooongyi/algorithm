def solution(arr):
  arr.remove(min(arr))
  if not len(arr):
    return [-1]
  return arr

print(solution([4, 3, 2, 1]))
print(solution([10]))