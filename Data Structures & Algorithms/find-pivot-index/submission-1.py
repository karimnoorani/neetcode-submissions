class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        curSum = 0

        for i, n in enumerate(nums):
            if curSum == total-curSum-n:
                return i
            curSum += n
        
        return -1