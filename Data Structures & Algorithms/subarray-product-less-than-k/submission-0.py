class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        curProduct = 1
        L = 0
        res = 0
        for R in range(len(nums)):
            curProduct *= nums[R]
            while L < R+1 and curProduct >= k:
                curProduct //= nums[L]
                L += 1
            res += R-L+1
        return res