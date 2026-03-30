import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)

        i = 1
        while i < k:
            heapq.heappop(nums)
            i += 1
        
        return -heapq.heappop(nums)