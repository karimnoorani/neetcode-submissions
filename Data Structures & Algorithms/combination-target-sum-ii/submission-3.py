class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        path = []
        res = []

        def dfs(i, total):
            if total == target:
                res.append(path[:])
                return
            
            if i >= len(nums) or total > target:
                return
            
            path.append(nums[i])
            dfs(i+1, total+nums[i])
            path.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            dfs(i, total)
        
        dfs(0, 0)
        return res