import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        
        heap = []
        for num in countMap:
            heapq.heappush(heap, [countMap[num], num])
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for numList in heap:
            res.append(numList[1])
        
        return res