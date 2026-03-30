class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        L = 0
        total = 0
        res = 1
        for R in range(len(nums)):
            total += nums[R]
            while nums[R]*(R-L+1) > total+k:
                total -= nums[L]
                L += 1
            res = max(res, R-L+1)
        
        return res