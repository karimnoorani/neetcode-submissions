class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minVal, maxVal = 1, 1
        res = max(nums)
        for n in nums:
            if n == 0:
                minVal, maxVal = 1, 1
                continue
            minVal, maxVal = min(minVal*n, maxVal*n, n), max(minVal*n, maxVal*n, n)
            res = max(res, maxVal)
        
        return res
