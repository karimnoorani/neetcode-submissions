class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}

        for c in s:
            sMap[c] = sMap.get(c, 0) + 1
        
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        
        if len(sMap) != len(tMap):
            return False
        
        for c in sMap:
            if sMap[c] != tMap.get(c, 0):
                return False
        
        return True