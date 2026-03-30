class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, lastNum):
            if i == len(nums):
                return 0
            
            if nums[i] <= lastNum:
                return dfs(i+1, lastNum)
            
            return max(1+dfs(i+1, nums[i]), dfs(i+1, lastNum))
        
        return dfs(0, -float('INF'))