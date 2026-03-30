import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        heap = []

        for num in count:
            heapq.heappush(heap, [count[num], num])
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for item in heap:
            res.append(item[1])
        
        return res