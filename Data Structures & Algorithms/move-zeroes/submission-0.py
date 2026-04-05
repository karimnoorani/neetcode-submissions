class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        L = 0
        for R in range(len(nums)):
            if nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
        """
        Do not return anything, modify nums in-place instead.
        """
        