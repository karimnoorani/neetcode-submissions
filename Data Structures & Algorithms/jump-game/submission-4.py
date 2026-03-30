class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def dfs(i):
            if i == len(nums)-1:
                return True
            
            if i >= len(nums) or nums[i] == 0:
                return False
            
            if i in cache:
                return cache[i]
            
            res = False
            for j in range(1, nums[i]+1):
                res = res or dfs(i+j)
            cache[i] = res
            return cache[i]
        
        return dfs(0)