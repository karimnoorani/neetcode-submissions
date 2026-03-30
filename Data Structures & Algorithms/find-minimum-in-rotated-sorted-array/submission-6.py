class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        res = float('INF')
        while L <= R:
            M = (L+R)//2

            if nums[L] <= nums[R]:
                return min(res, nums[L])
            
            if nums[L] <= nums[M]:
                res = min(res, nums[L])
                L = M + 1
            else:
                res = min(res, nums[M])
                R = M - 1
