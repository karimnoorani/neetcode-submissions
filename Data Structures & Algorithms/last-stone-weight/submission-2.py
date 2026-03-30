import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            max1 = -heapq.heappop(stones)
            max2 = -heapq.heappop(stones)

            if max1 > max2:
                heapq.heappush(stones, -1*(max1-max2))
            elif max2 > max1:
                heapq.heappush(stones, -1*(max2-max1))
        
        if len(stones) == 0:
            return 0
        
        return -heapq.heappop(stones)