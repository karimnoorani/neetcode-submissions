class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(total):
            if total == amount:
                return 0
            
            if total > amount:
                return float('INF')

            if total in cache:
                return cache[total]
            
            res = float('INF')
            for c in coins:
                res = min(res, 1+dfs(total+c))
            cache[total] = res
            
            return cache[total]
        
        res = dfs(0)
        return res if res < float('INF') else -1