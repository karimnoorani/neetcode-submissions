import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        items = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        heap = []
        res = []
        for count, c in items:
            if count != 0:
                heapq.heappush(heap, [count, c])
        
        reappend = None
        while heap:
            if len(res) > 1 and res[-1] == res[-2] == heap[0][1]:
                reappend = heapq.heappop(heap)
                if len(heap) == 0:
                    break
            
            count, c = heapq.heappop(heap)
            res.append(c)
            if count+1 != 0:
                heapq.heappush(heap, [count+1, c])
            
            if reappend:
                heapq.heappush(heap, reappend)
                reappend = None
        
        return "".join(res)