class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0 or len(nums) == 1:
            return False
        
        cache = {}
        def dfs(i, total):
            if total == sum(nums)//2:
                cache[(i, total)] = True
                return cache[(i, total)]
            
            if i == len(nums):
                return False
            
            if (i, total) in cache:
                return cache[(i, total)]
            
            cache[(i, total)] = dfs(i+1, total) or dfs(i+1, total+nums[i])
            return cache[(i, total)]
        
        return dfs(0, 0)
        