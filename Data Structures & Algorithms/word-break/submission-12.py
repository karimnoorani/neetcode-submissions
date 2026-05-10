class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        wordDict = set(wordDict)

        for i in range(len(dp)-1, -1, -1):
            if s[i:] in wordDict:
                dp[i] = True
                continue
            
            for j in range(i+1, len(s)):
                if dp[j] and s[i:j] in wordDict:
                    dp[i] = True
                    break
        
        return dp[0]