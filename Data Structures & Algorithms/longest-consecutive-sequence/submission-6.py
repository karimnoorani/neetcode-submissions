class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()
        
        for num in nums:
            numsSet.add(num)
        
        lcs = 0
        for num in numsSet:
            if num-1 not in numsSet:
                currentSeq = 1
                
                while num+currentSeq in numsSet:
                    currentSeq += 1
                
                lcs = max(lcs, currentSeq)
        
        return lcs