class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount = 0
        L = 0
        res = 0
        for R in range(len(nums)):
            zeroCount += 1 if nums[R] == 0 else 0
            while zeroCount > k:
                zeroCount += -1 if nums[L] == 0 else 0
                L += 1
            res = max(res, R-L+1)
        return res