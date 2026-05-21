class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        max_heap = [-num for num in nums]
        min_heap = nums[:]

        heapq.heapify(max_heap)
        heapq.heapify(min_heap)

        i = 0
        while i < len(nums):
            nums[i] = heapq.heappop(min_heap)
            if i + 1 < len(nums):
                nums[i+1] = -heapq.heappop(max_heap)
            i += 2
        """
        Do not return anything, modify nums in-place instead.
        """
        