class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i, target):
            if (i, target) in cache:
                return cache[(i, target)]
            
            if target == 0:
                cache[(i, target)] = 0
                return cache[(i, target)]
            
            if i == len(coins) or target < 0:
                return float('INF')
            
            add = 1+dfs(i, target-coins[i])
            skip = dfs(i+1, target)
            
            cache[(i, target)] = min(add, skip)
            return cache[(i, target)]
            
        
        count = dfs(0, amount)
        return count if count < float('INF') else -1