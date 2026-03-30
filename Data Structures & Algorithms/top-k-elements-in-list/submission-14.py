class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        heap = []

        for n in freqMap:
            heapq.heappush(heap, [freqMap[n], n])
            if len(heap) > k:
                heapq.heappop(heap)

        res = [x[1] for x in heap]
        return res           