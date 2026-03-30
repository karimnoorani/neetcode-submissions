import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        res = []

        for num in nums:
            heapq.heappush(heap, num)
        
        while heap:
            res.append(heapq.heappop(heap))
        
        return res