class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cache = {}

        def dfs(L, R, k):
            if k == 0:
                return 0
            
            if (L, R, k) in cache:
                return cache[(L, R, k)]
            
            cache[(L, R, k)] = max(cardPoints[L]+dfs(L+1, R, k-1), cardPoints[R]+dfs(L, R-1, k-1))
            return cache[(L, R, k)]
        
        return dfs(0, len(cardPoints)-1, k)
