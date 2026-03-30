class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        
        def dfs(i, j):
            if i > j:
                return 0
            
            if (i, j) not in cache:
                if i == 0:
                    cache[(i, j)] = max(nums[i] + dfs(i+2, j-1), dfs(i+1, j))
                else:
                    cache[(i, j)] = max(nums[i] + dfs(i+2, j), dfs(i+1, j))
            
            return cache[(i, j)]
        
        return dfs(0, len(nums)-1)