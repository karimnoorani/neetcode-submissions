class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in cache:
                return cache[(l, r)]
            
            first = piles[l]-dfs(l+1, r)
            last = piles[r]-dfs(l, r-1)
            
            cache[(l, r)] = max(first, last)
            return cache[(l, r)]
        
        return dfs(0, len(piles)-1) > 0
