class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums)-1:
                return 0
            
            if nums[i] == 0:
                return float('INF')
            if i in cache:
                return cache[i]
            
            res = float('INF')
            for j in range(1, nums[i]+1):
                res = min(res, 1+dfs(i+j))
            
            cache[i] = res
            return res
        
        return dfs(0)
            