class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        res = float('-INF')

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            res = max(res, curSum)
        
        return res