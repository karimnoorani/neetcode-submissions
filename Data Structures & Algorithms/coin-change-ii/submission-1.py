class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, total):
            if total == amount:
                return 1
            
            if i == len(coins) or total > amount:
                return 0
            
            if (i, total) in cache:
                return cache[(i, total)]
            
            skip = dfs(i+1, total)
            include = dfs(i, total+coins[i])

            cache[(i, total)] = skip + include

            return cache[(i, total)]
        
        return dfs(0, 0)