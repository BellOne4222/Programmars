import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    mix = 0
    
    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1
        if scoville[0] >= K:
            return mix
            break
            
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b*2))
        mix += 1
        
    return mix