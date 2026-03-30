class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, currentSum):
            if i == len(nums):
                if currentSum == target: return 1
                else: return 0
            
            if (i, currentSum) in cache:
                return cache[(i, currentSum)]
            
            cache[(i, currentSum)] = dfs(i+1, currentSum+nums[i]) + dfs(i+1, currentSum-nums[i])
            return cache[(i, currentSum)]
        
        return dfs(0, 0)