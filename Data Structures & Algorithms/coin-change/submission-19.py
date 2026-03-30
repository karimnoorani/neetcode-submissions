class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(target):
            if target == 0:
                return 0

            if target < 0:
                return float('INF')
            
            if target in cache:
                return cache[target]
            
            minCoins = float('INF')
            for c in coins:
                minCoins = min(minCoins, 1+dfs(target-c))
            
            cache[target] = minCoins
            return cache[target]
        
        res = dfs(amount)
        return res if res < float('INF') else -1