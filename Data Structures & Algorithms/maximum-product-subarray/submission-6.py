class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        res = max(nums)

        for num in nums:
            if num == 0:
                curMax = curMin = 1
                continue
            tmp = curMax * num
            curMax = max(curMax*num, curMin*num, num)
            curMin = min(tmp, curMin*num, num)
            res = max(res, curMax)
        
        return res