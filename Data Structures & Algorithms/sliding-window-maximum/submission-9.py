import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []

        for R in range(len(nums)):
            heapq.heappush(heap, [-nums[R], R])

            while heap[0][1] <= R-k:
                heapq.heappop(heap)

            if R >= k-1:
                res.append(-heap[0][0])
        
        return res