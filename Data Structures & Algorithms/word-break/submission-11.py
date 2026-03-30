class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        cache = {}
        
        def dfs(i):
            if i == len(s):
                return True
            
            if i in cache:
                return cache[i]
            
            res = False
            for j in range(i+1, len(s)+1):
                if s[i:j] not in wordDict:
                    continue
                res = res or dfs(j)
            cache[i] = res

            return cache[i]
        
        
        return dfs(0)
