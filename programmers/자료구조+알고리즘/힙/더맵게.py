import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K and len(scoville) > 1:
        answer += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        
    if scoville[0] < K:
        return -1
    
    return answer