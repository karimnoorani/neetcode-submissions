import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        heap = []
        res = []

        for num in nums:
            numsMap[num] = numsMap.get(num, 0) + 1
        
        for num in numsMap:
            heapq.heappush(heap, [-numsMap[num], num])
        
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res