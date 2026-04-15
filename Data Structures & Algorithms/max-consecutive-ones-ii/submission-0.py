class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        freq = {0: 0, 1: 0}
        L = 0
        res = 0

        for R in range(len(nums)):
            freq[nums[R]] += 1

            while freq[0] > 1:
                freq[nums[L]] -= 1
                L += 1
            
            res = max(res, R-L+1)
        
        return res