class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        def dfs(l, r):
            if (l, r) in cache:
                return cache[(l, r)]
            res = 0
            for i in range(l, r+1):
                res = max(res, dfs(l, i-1)+nums[l-1]*nums[i]*nums[r+1]+dfs(i+1, r))
            cache[(l, r)] = res
            return cache[(l, r)]
        
        return dfs(1, len(nums)-2)