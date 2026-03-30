class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            n = nums[i]
            if nums[i] <= 0 or i == n-1 or nums[i] > len(nums) or nums[n-1] == nums[i]:
                i += 1
            else:
                nums[n-1], nums[i] = nums[i], nums[n-1]
        
        for i, n in enumerate(nums):
            if i+1 != n:
                return i+1
        
        return len(nums)+1
            