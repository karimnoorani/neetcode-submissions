class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        i = 1
        while i < len(nums)-1:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 2
        """
        Do not return anything, modify nums in-place instead.
        """
        