class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(total):
            if total == target:
                return 1
            
            if total > target:
                return 0

            if total in cache:
                return cache[total]

            res = 0
            for n in nums:
                res += dfs(total+n)
            cache[total] = res
            return cache[total]
        
        return dfs(0)