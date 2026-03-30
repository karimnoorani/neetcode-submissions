class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        longest = s[0]
        for i in range(len(s)+1):
            for j in range(i+1, len(s)+1):
                if len(longest) < j-i and isPalindrome(s[i:j]):
                    longest = s[i:j]
        
        return longest