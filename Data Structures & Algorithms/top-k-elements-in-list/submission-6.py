import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = Counter(nums) # O(n)
        heap = []

        for num in numsMap:
            heapq.heappush(heap, [numsMap[num], num]) # log(k)
            if len(heap) > k:
                heapq.heappop(heap) # log (k)
        
        res = []
        for numList in heap:
            res.append(numList[1]) # O(n)
        
        return res