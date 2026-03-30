class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charSet = {}

        for c in s:
            charSet[c] = charSet.get(c, 0) + 1
        
        comparisonSet = {}
        for c in t:
            comparisonSet[c] = comparisonSet.get(c, 0) + 1
        
        for c in charSet:
            if charSet[c] != comparisonSet.get(c, 0):
                return False
        
        return True