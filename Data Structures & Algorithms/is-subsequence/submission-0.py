class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sP = 0

        for tP in range(len(t)):
            if sP == len(s):
                return True
            
            sP += 1 if s[sP] == t[tP] else 0
        
        return True if sP == len(s) else False