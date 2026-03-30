from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i, total):
            if total == amount:
                return 0
            
            if i == len(coins) or total > amount:
                return float('inf')
            
            if (i, total) in cache:
                return cache[(i, total)]

            skip = dfs(i+1, total)
            include = 1 + dfs(i, total+coins[i])
            
            cache[(i, total)] = min(skip, include)

            return cache[(i, total)]
            
        res = dfs(0, 0)
        return res if res < float('inf') else -1