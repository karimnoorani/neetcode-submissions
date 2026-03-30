class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        L, R = 0, len(nums)-1
        for i in range(len(res)-1, -1, -1):
            if abs(nums[L]) > abs(nums[R]):
                res[i] = nums[L] * nums[L]
                L += 1
            else:
                res[i] = nums[R] * nums[R]
                R -= 1
        return res