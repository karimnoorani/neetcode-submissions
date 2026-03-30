class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        cache = {len(s): True}
        def dfs(i):
            if i in cache:
                return cache[i]
            
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict and dfs(j):
                    cache[i] = True
                    return cache[i]
            
            cache[i] = False
            return cache[i]
        
        return dfs(0)