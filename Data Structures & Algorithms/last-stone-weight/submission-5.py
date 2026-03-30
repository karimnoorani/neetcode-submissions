import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            rock1 = -heapq.heappop(stones)
            rock2 = -heapq.heappop(stones)

            if rock1 > rock2:
                heapq.heappush(stones, (rock1-rock2)*-1)
        
        return -stones[0] if len(stones) > 0 else 0