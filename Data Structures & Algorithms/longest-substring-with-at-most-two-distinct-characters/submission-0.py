class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        charMap = defaultdict(int)
        count = 0
        res = 0
        L = 0

        for R in range(len(s)):
            charMap[s[R]] += 1
            count += 1 if charMap[s[R]] == 1 else 0

            while count > 2:
                charMap[s[L]] -= 1
                count += -1 if charMap[s[L]] == 0 else 0
                L += 1
            
            res = max(res, R-L+1)
        
        return res