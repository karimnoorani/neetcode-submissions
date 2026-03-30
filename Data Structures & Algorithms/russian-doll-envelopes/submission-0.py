class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        cache = {}

        def dfs(w, h):
            if (w, h) in cache:
                return cache[(w, h)]
            
            res = 1
            for w2, h2 in envelopes:
                if w > w2 and h > h2:
                    res = max(res, 1+dfs(w2, h2))
            cache[(w, h)] = res
            return cache[(w, h)]
        
        res = 1
        for w, h in envelopes:
            res = max(res, dfs(w, h))
        
        return res