class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = Counter(s1)
        s1length = len(s1)
        s2map = defaultdict(int)

        for index in range(len(s2)):
            s2map[s2[index]] += 1
            
            if index >= s1length:
                s2map[s2[index-s1length]] -= 1

                if s2map[s2[index-s1length]] == 0:
                    del s2map[s2[index-s1length]]
            
            if s1map == s2map:
                return True
        
        return False