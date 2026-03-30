class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        count = 0
        sMap = defaultdict(int)
        L = 0
        res = ""
        resLen = float('inf')
        for R in range(len(s)):
            sMap[s[R]] += 1
            count += 1 if s[R] in tMap and sMap[s[R]] == tMap[s[R]] else 0

            while count == len(tMap):
                if R-L+1 < resLen:
                    res = s[L:R+1]
                    resLen = R-L+1
                
                sMap[s[L]] -= 1
                count += -1 if s[L] in tMap and sMap[s[L]] < tMap[s[L]] else 0
                L += 1
        
        return res