import heapq

# heapq는 요소의 삭제, 추가마다 자동으로 정렬해준다. -> 정렬에 따로 비용이 들지 않는다.

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while heap[0] < K:
        try: 
            firstItem = heapq.heappop(heap)
            secondItem = heapq.heappop(heap)

            heapq.heappush(heap, firstItem + 2 * secondItem)
            answer += 1
        except IndexError:
            return -1 
    return answer