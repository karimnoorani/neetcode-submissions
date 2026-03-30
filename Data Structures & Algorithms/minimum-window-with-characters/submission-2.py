class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        
        l, shortestString, sMap = 0, "", {}
        
        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1

            if self.containsLetters(tMap, sMap.copy(), ""):
                while self.containsLetters(tMap, sMap.copy(), s[l]):
                    sMap[s[l]] -= 1
                    l += 1
                print(s[l], s[r], l , r)
                if shortestString == "" or len(shortestString) > (r-l+1):
                    shortestString = s[l:r+1]
        
        return shortestString

    def containsLetters(self, tMap, sMap, letterToRemove):
        if letterToRemove != "":
            sMap[letterToRemove] -= 1

        for c in tMap:
            if sMap.get(c, 0) < tMap[c]:
                return False
        
        return True