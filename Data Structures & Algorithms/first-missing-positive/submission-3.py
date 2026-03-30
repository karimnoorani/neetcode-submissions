class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = 0 if nums[i] < 0 else nums[i]
        
        for i, n in enumerate(nums):
            if abs(n) <= len(nums) and n != 0:
                if nums[abs(n)-1] == 0:
                    nums[abs(n)-1] = (len(nums)+1)*-1
                else:
                    nums[abs(n)-1] = -1*abs(nums[abs(n)-1])

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        
        return len(nums)+1