class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        cache = {}
        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in cache:
                return cache[(l, r)]
            
            if l == r:
                return nums[l]*nums[l-1]*nums[r+1]
            
            res = 0
            for i in range(l, r+1):
                res = max(res, nums[l-1]*nums[i]*nums[r+1]+dfs(i+1, r)+dfs(l, i-1))
            cache[(l, r)] = res

            return res
        
        return dfs(1, len(nums)-2)