class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        res = nums[0]

        while L <= R:
            if nums[L] < nums[R]:
                return min(res, nums[L])
            
            M = (L+R)//2
            res = min(res, nums[M])
            if nums[M] >= nums[L]:
                L = M + 1
            else:
                R = M - 1
        
        return res
