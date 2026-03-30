from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = Counter(s1)
        
        l, r = 0, len(s1)
        while r <= len(s2):
            if Counter(s2[l:r]) == s1count:
                return True
            l += 1
            r += 1
        
        return False