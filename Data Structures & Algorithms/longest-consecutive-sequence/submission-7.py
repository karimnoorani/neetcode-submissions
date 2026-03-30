class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxSeq = 0

        for num in numsSet:
            if (num-1) not in numsSet:
                curSeq = 1
                val = num + 1
                while val in numsSet:
                    curSeq += 1
                    val += 1
                maxSeq = max(maxSeq, curSeq)
        
        return maxSeq
                