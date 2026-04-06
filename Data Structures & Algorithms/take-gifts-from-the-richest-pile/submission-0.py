import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for g in gifts:
            heapq.heappush(heap, -g)
        
        while k > 0:
            g = -heapq.heappop(heap)
            heapq.heappush(heap, -math.floor(g ** 0.5))
            k -= 1
        
        res = 0
        while heap:
            res += -heapq.heappop(heap)
        
        return res