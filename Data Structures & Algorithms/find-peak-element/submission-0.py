class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        L, R = 1, len(nums)-2

        while L <= R:
            M = (L + R) // 2

            if nums[M+1] > nums[M]:
                L = M + 1
            elif nums[M-1] > nums[M]:
                R = M - 1
            elif nums[M+1] == nums[M] == nums[M-1]:
                L = M + 1
            else:
                return M-1