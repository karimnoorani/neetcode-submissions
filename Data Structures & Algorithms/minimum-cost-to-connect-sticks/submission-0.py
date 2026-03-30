class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minHeap = []
        res = 0

        for s in sticks:
            heapq.heappush(minHeap, s)
        
        while len(minHeap) > 1:
            total = heapq.heappop(minHeap) + heapq.heappop(minHeap)
            res += total
            heapq.heappush(minHeap, total)
        
        return res