class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        cache = {}
        def dfs(w, h):
            if (w, h) in cache:
                return cache[(w, h)]
            
            res = 1
            for w1, h1 in envelopes:
                if w > w1 and h > h1:
                    res = max(res, 1+dfs(w1, h1))
            cache[(w, h)] = res
            
            return cache[(w, h)]
        
        res = 1
        for w, h in envelopes:
            res = max(res, dfs(w, h))
        
        return res