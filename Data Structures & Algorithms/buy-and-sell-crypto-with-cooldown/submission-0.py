class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            
            if (i, canBuy) in cache:
                return cache[(i, canBuy)]

            if not canBuy:
                cache[(i, canBuy)] = max(dfs(i+1, False), prices[i]+dfs(i+2, True))
                return cache[(i, canBuy)]
            
            cache[(i, canBuy)] = max(dfs(i+1, True), dfs(i+1, False)-prices[i])
            return cache[(i, canBuy)]
        
        return dfs(0, True)