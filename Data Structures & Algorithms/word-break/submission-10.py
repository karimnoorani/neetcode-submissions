class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        cache = {}
        
        def dfs(i, j):
            if i == len(s):
                return True
            
            if j == len(s)+1:
                return False
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            take = dfs(j, j+1) if s[i:j] in wordDict else False
            skip = dfs(i, j+1)

            cache[(i, j)] = take or skip
            return cache[(i, j)]
        
        return dfs(0, 1)
