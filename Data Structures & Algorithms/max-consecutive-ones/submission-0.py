class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        streak = 0
        for n in nums:
            streak = streak + 1 if n == 1 else 0
            res = max(res, streak)
        return res