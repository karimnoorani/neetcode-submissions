class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tP = 0

        for sP in range(len(s)):
            if tP == len(t):
                return 0
            
            if s[sP] == t[tP]:
                tP += 1
        
        return len(t)-tP