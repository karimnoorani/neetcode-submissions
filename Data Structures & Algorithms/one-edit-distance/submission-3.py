class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s)-len(t)) > 1:
            return False
        
        foundDiff = False
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if foundDiff:
                    return False
                
                foundDiff = True

                if len(s) >= len(t):
                    i += 1
                    if len(s) > len(t):
                        continue
            else:
                i += 1
            
            j += 1
        
        res = foundDiff or (not foundDiff and (j == len(t)-1 or i == len(s)-1))
        return res