class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        cache = {len(s): 0}
        def dfs(i):
            if i in cache:
                return cache[i]
            
            res = 1 + dfs(i+1)
            for j in range(i+1, len(s)+1):
                w = s[i:j]
                if w in words:
                    res = min(res, dfs(j))
            cache[i] = res
            return res
        
        return dfs(0)