class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0 
        L = 0
        res = 100001

        for R in range(len(nums)):
            total += nums[R]
            
            while total-nums[L] >= target:
                total -= nums[L]
                L += 1

            if total >= target:
                res = min(res, R-L+1)
            
        return res if res < 100001 else 0