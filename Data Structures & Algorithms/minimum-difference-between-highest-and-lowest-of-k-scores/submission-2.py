class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        res = float('INF')
        
        for i in range(k-1, len(nums)):
            res = min(res, nums[i]-nums[i-k+1])
        
        return res