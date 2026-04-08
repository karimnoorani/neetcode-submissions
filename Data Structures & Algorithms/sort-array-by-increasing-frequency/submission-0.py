class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {n: 0 for n in set(nums)}
        
        for n in nums:
            freq[n] += 1
        
        heap = []
        for n in freq:
            heapq.heappush(heap, [freq[n], -n])
        
        res = []
        while heap:
            i, n = heapq.heappop(heap)
            for _ in range(i):
                res.append(-n)
        
        return res