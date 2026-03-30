class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, total):
            if total == target:
                res.append(subset[:])
                return
            
            if i == len(nums) or total > target:
                return
            
            dfs(i+1, total)

            iterations = 0
            while total < target:
                subset.append(nums[i])
                total += nums[i]
                iterations += 1
                dfs(i+1, total)
            
            for _ in range(iterations):
                subset.pop()

            
        
        dfs(0, 0)
        return res