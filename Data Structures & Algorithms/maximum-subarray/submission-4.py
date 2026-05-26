class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        res = nums[0]
        for num in nums[1:]:
            if total < 0:
                total = 0
            
            total += num
            res = max(res, total)
        return res