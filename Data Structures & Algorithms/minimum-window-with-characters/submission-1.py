class Solution:
    def checkIfSatisfies(self, charT, charSub, charToRemove):
        charSubCopy = charSub.copy()
        
        if charToRemove != None:
            charSubCopy[charToRemove] -= 1

        for c in charT:
            if charT[c] > charSubCopy.get(c, 0):
                return False
        
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        charT = {}
        for c in t:
            charT[c] = 1 + charT.get(c, 0)
        
        shortestString = ""
        l = 0
        charSub = {}
        for r in range(len(s)):
            charSub[s[r]] = 1 + charSub.get(s[r], 0)
            
            while self.checkIfSatisfies(charT, charSub, s[l]):
                charSub[s[l]] -= 1
                l += 1

            if self.checkIfSatisfies(charT, charSub, None):
                if shortestString == "" or len(shortestString) > (r-l+1):
                    shortestString = s[l:r+1]
        
        return shortestString
