class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            L, R = i+1, len(nums)-1

            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total >= target:
                    R -= 1
                else:
                    res += R-L
                    L += 1
        return res