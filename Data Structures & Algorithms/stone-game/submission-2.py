class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        def dfs(l, r):
            if l == r:
                return piles[l]
            
            if (l, r) in cache:
                return cache[(l, r)]
            
            cache[(l, r)] = max(piles[l]-dfs(l+1, r), piles[r]-dfs(l, r-1))
            return cache[(l, r)]
        
        res = dfs(0, len(piles)-1)
        return res > 0