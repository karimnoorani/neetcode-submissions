import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num in freq:
            heapq.heappush(min_heap, [freq[num], num])
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = [item[1] for item in min_heap]

        return result