class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}

        def dfs(i, M):
            if i == len(piles):
                return 0
            
            if (i, M) in cache:
                return cache[(i, M)]
            
            best = float('-INF')
            total = 0
            for X in range(1, 2*M+1):
                if i + X > len(piles):
                    break
                total += piles[i+X-1]
                best = max(best, total+dfs(i+X, max(M, X)))
            
            cache[(i, M)] = sum(piles[i:])-best
            return cache[(i, M)]
        
        return sum(piles)-dfs(0, 1)
            
