class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()

        for num in nums:
            numsSet.add(num)
        
        maxSeq = 0
        for num in nums:
            r = num + 1
            currentSeq = 1
            while r in numsSet:
                currentSeq += 1
                r += 1
            maxSeq = max(maxSeq, currentSeq)
        
        return maxSeq