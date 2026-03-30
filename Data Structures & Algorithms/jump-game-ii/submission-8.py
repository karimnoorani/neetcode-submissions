class Solution:
    def jump(self, nums: List[int]) -> int:
        L, R, res = 0, 0, 0

        while L <= R:
            farthest = R
            for i in range(L, R+1):
                if i == len(nums)-1:
                    return res
                farthest = max(farthest, i+nums[i])
            L = R + 1
            R = farthest
            res += 1