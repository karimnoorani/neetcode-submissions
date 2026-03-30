class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = Counter(s1)
        s2Map = defaultdict(int)
        L = 0
        count = 0
        for R in range(len(s2)):
            s2Map[s2[R]] += 1
            
            if s2Map[s2[R]] == s1Map.get(s2[R], 0):
                count += 1
            
            if R - L + 1 > len(s1):
                if s2Map[s2[L]] == s1Map.get(s2[L], 0):
                    count -= 1
                s2Map[s2[L]] -= 1
                L += 1
            
            if count == len(s1Map):
                return True
        
        return False