from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charMap = Counter(s1)
        
        for i in range(len(s1), len(s2)+1):
            print(Counter(s2[i-len(s1):i]))
            if charMap == Counter(s2[i-len(s1):i]):
                return True
        
        return False