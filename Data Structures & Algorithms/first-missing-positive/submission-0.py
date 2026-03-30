class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1

        for n in nums:
            if res == n:
                res += 1
            if n > res:
                break

        return res 