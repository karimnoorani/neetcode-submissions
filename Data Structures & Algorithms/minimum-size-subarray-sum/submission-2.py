class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        total = 0
        res = float('INF')

        for R in range(len(nums)):
            total += nums[R]

            while total >= target:
                res = min(res, R-L+1)
                total -= nums[L]
                L += 1
        
        return res if res != float('INF') else 0