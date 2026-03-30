class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for c1, c2 in zip(s, t):
            sMap[c1] += 1
            tMap[c2] += 1
        
        return sMap == tMap