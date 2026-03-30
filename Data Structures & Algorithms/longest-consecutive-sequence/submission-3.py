class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        LCS = 0
        
        for num in nums:
            if (num-1) not in numsSet:
                currentSeq = 1
                while (num+1) in numsSet:
                    currentSeq += 1
                    num += 1
                LCS = max(LCS, currentSeq)
        
        return LCS