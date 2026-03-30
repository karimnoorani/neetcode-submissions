class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i, prev):
            if i == len(nums):
                return 0
            
            if nums[i] <= prev:
                return dfs(i+1, prev)

            if (i, prev) in cache:
                return cache[(i, prev)]

            cache[(i, prev)] = max(dfs(i+1, prev), 1+dfs(i+1, nums[i]))
            return cache[(i, prev)]
        
        return dfs(0, float('-INF'))