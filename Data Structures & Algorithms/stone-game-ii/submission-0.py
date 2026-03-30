class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}
        def dfs(alice, i, m):
            if i == len(piles):
                return 0
            
            if (alice, i, m) in cache:
                return cache[(alice, i, m)]
            
            res = 0 if alice else float("INF")
            total = 0
            for X in range(1, (2*m)+1):
                if i + X > len(piles):
                    break
                total += piles[i+X-1]
                if alice:
                    res = max(res, total+dfs(False,i+X, max(m, X)))
                else:
                    res = min(res, dfs(True, i+X, max(m, X)))
            cache[(alice, i, m)] = res
            return cache[(alice, i, m)]
        
        return dfs(True, 0, 1)
                
                