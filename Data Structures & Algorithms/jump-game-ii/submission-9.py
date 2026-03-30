class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i == len(nums)-1:
                return 0
            
            if i >= len(nums):
                return float('INF')

            if i in cache:
                return cache[i]
            
            res = float('INF')
            for j in range(i+1, i+nums[i]+1):
                res = min(res, 1+dfs(j))
            
            cache[i] = res
            return res
        
        return dfs(0)
        
