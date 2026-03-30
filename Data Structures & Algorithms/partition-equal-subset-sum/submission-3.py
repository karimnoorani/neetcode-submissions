class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums)//2

        def dfs(i, total):
            if total == target:
                return True
            
            if i == len(nums) or total > target:
                return False
            
            add = dfs(i+1, total+nums[i])
            skip = dfs(i+1, total)

            return add or skip
        
        return dfs(0, 0)