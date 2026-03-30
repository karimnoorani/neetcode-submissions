import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            stone1 = heapq.heappop(stones)*-1
            stone2 = heapq.heappop(stones)*-1

            if stone1 != stone2:
                heapq.heappush(stones,(stone1-stone2)*-1)
        
        return -stones[0] if len(stones) > 0 else 0