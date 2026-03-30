import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        freqMap = defaultdict(int)
        heap = []
        reappend = []

        for c in s:
            freqMap[c] += 1
        
        for c, count in freqMap.items():
            heapq.heappush(heap, [-count, c])
        
        while heap:
            if res and res[-1] == heap[0][1]:
                reappend.append(heapq.heappop(heap))
            
            if len(heap) == 0:
                return ""
            
            count, c = heapq.heappop(heap)
            res.append(c)
            reappend.append([count+1, c])

            while reappend:
                count, c = reappend.pop()
                if count != 0:
                    heapq.heappush(heap, [count, c])
        
        return "".join(res)