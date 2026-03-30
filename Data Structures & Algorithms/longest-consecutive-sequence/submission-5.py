class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        LCS = 0
        for num in numsSet:
            if num-1 not in numsSet:
                currentSeq = 1
                i = 1
                while (num+i) in numsSet:
                    i += 1
                    currentSeq += 1
                LCS = max(LCS, currentSeq)
        
        return LCS
                