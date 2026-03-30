class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        res = nums[0]
        
        for n in nums[1:]:
            if curSum < 0:
                curSum = 0
            
            curSum += n
            res = max(res, curSum)
        
        return res