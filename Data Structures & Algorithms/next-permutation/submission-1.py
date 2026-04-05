class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pivot = None
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        
        if pivot == None:
            nums.reverse()
            return
        
        swap_i = pivot + 1
        for i in range(pivot+1, len(nums)):
            if nums[i] <= nums[swap_i] and nums[i] > nums[pivot]:
                swap_i = i
        
        nums[swap_i], nums[pivot] = nums[pivot], nums[swap_i]
        nums[pivot+1:] = reversed(nums[pivot+1:])

        """
        Do not return anything, modify nums in-place instead.
        """
