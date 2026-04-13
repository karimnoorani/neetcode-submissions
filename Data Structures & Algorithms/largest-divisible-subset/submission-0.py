class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            
            res = [nums[i]]
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    path = dfs(j)
                    if 1+len(path) > len(res):
                        res = [nums[i]] + path
            cache[i] = res
            return cache[i]
        
        res = [nums[0]]
        for i in range(len(nums)):
            path = dfs(i)
            if len(path) > len(res):
                res = path
        return res