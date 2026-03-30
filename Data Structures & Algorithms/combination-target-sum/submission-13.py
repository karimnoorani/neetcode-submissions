class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i, currentSum):
            if i >= len(nums):
                print(subset, currentSum)
                if currentSum == target:
                    res.append(subset.copy())
                return
            
            while currentSum <= target:
                dfs(i+1, currentSum)
                subset.append(nums[i])
                currentSum += nums[i]

            while len(subset) > 0 and subset[-1] == nums[i]:
                subset.pop()
            
        dfs(0, 0)

        return res