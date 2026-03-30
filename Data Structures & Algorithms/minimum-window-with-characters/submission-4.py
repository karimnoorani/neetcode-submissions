class Solution:
    def minWindow(self, s: str, t: str) -> str:
        L = 0
        tMap = Counter(t)
        sMap = defaultdict(int)
        count = 0
        res = ""
        resLen = float('INF')
        for R in range(len(s)):
            sMap[s[R]] += 1
            if sMap[s[R]] == tMap.get(s[R], 0):
                count += 1
            
            while count == len(tMap):
                if R-L+1 < resLen:
                    res = s[L:R+1]
                    resLen = R-L+1
                
                sMap[s[L]] -= 1
                if sMap[s[L]] < tMap.get(s[L], 0):
                    count -= 1
                
                L += 1
        
        return res