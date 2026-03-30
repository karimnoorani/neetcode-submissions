class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        l = 0
        maxLength = 0
        
        for r in range(len(s)):
            charDict[s[r]] = charDict.get(s[r], 0) + 1

            while (r-l+1) - max(charDict.values()) > k:
                charDict[s[l]] -= 1
                l += 1
            
            maxLength = max(maxLength, r-l+1)
        
        return maxLength