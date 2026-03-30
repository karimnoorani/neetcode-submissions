class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}
        wordDict = set(wordDict)

        def dfs(i):
            if i == len(s):
                return [""]
            
            if i in cache:
                return cache[i]
            
            res = []
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    for w in dfs(j):
                        res.append(s[i:j] + " " + w if w != "" else s[i:j])
            cache[i] = res
            return cache[i]
        
        return dfs(0)