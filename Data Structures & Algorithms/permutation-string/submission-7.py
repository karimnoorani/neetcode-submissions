class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        
        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1
        
        l = 0
        s2Map = {}
        minLength = len(s1)+1
        for r in range(len(s2)):
            s2Map[s2[r]] = s2Map.get(s2[r], 0) + 1

            if self.containsLetters(s1Map, s2Map, None):
                while self.containsLetters(s1Map, s2Map, s2[l]):
                    s2Map[s2[l]] -= 1
                    l += 1
                print(s2[l], s2[r])
                minLength = min(minLength, r-l+1)
        
        return minLength == len(s1)

    def containsLetters(self, s1Map: dict, s2Map: dict, letterToRemove: str) -> bool:
        s2MapCopy = s2Map.copy()
        if letterToRemove is not None:
            s2MapCopy[letterToRemove] -= 1
        for c in s1Map:
            if s2MapCopy.get(c, 0) < s1Map[c]:
                return False
        
        return True