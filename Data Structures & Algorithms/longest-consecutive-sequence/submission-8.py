class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        LCS = 0
        for n in nums:
            if n-1 in numsSet:
                continue
            
            l = 1
            while n+1 in numsSet:
                l, n = l + 1, n + 1
            
            LCS = max(LCS, l)
        
        return LCS