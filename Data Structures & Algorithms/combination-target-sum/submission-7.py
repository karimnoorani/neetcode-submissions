class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currentSum, subset):
            if i >= len(nums):
                print(subset, currentSum)
                if currentSum == target:
                    res.append(subset)
                return
            
            while currentSum <= target:
                dfs(i+1, currentSum, subset.copy())
                subset.append(nums[i])
                currentSum += nums[i]
        
        dfs(0, 0, [])

        return res