class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        mod = 10**9 + 7
        for L in range(len(nums)):
            if nums[L] * 2 > target:
                break
            
            R = L
            while R + 1 < len(nums) and nums[R+1] + nums[L] <= target:
                R += 1
            
            res += 2**(R-L)
            res %= mod
        
        return res