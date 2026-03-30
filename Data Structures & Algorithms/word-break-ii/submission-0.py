class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        subStrings = []

        def backtrack(i):
            if i == len(s):
                res.append(" ".join(subStrings))
                return
            
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    subStrings.append(s[i:j])
                    backtrack(j)
                    subStrings.pop()
        
        backtrack(0)
        return res