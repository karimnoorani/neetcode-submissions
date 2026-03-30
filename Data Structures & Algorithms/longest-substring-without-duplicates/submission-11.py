class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        longest = 0
        cMap = {}

        for R in range(len(s)):
            L = max(L, cMap.get(s[R], -1)+1)
            longest = max(longest, R-L+1)
            cMap[s[R]] = R
        
        return longest