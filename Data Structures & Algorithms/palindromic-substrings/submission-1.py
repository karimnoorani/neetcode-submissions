class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)

        for i in range(len(s)):
            l, r = i-1, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res