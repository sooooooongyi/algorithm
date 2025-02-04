def puzzle(level, diffs, times):
    total = 0
    for i in range(len(diffs)):
        time = 0
        if level >= diffs[i]:
            time += times[i]
        else:
            time += (diffs[i] - level) * (times[i-1] + times[i]) + times[i]
        total += time
    return total
    

def solution(diffs, times, limit):
    start, end, mid = 1, max(diffs), 0    
    level = pow(10, 15)
    
    while start <= end:
        mid = (start + end)//2
        result = puzzle(mid, diffs, times)
        
        if result > limit:
            start = mid + 1
        else:
            end = mid - 1
            level = min(mid, level)
            
    return level