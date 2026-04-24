class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        heap = []
        for a, b in costs:
            res += a
            heapq.heappush(heap, b-a)
        
        for _ in range(len(costs)//2):
            res += heapq.heappop(heap)
        
        return res