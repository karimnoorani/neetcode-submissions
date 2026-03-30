from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = Counter(s)
        tMap = Counter(t)

        return sMap == tMap