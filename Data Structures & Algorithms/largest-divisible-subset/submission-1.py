class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            
            res = []
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    subset = dfs(j)
                    if len(subset) > len(res):
                        res = subset
            cache[i] = [nums[i]] + res
            return cache[i]
        
        res = []
        for i in range(len(nums)):
            subset = dfs(i)
            if len(subset) > len(res):
                res = subset
        
        return res