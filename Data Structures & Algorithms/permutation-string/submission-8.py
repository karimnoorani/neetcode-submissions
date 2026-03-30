class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = defaultdict(int)

        for c in s1:
            s1Map[c] += 1
        
        L = 0
        cMap = defaultdict(int)
        for R in range(len(s2)):
            cMap[s2[R]] += 1

            if R-L+1 > len(s1):
                cMap[s2[L]] -= 1
                if cMap[s2[L]] == 0:
                    del cMap[s2[L]]
                L += 1
            
            if cMap == s1Map:
                return True
        

        return False