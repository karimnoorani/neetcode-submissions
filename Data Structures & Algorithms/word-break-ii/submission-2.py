class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        path = []

        def dfs(i):
            if i == len(s):
                res.append(" ".join(path))
                return
            
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    path.append(s[i:j])
                    dfs(j)
                    path.pop()
        
        dfs(0)
        return res