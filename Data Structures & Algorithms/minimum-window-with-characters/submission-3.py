class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap, window = defaultdict(int), defaultdict(int)

        for c in t:
            tMap[c] += 1
        
        have, need = 0, len(tMap)

        res = ""
        resLen = float("infinity")
        L = 0 

        for R in range(len(s)):
            window[s[R]] += 1

            if s[R] in tMap and window[s[R]] == tMap[s[R]]:
                have += 1
            
            while have == need:
                if R-L+1 < resLen:
                    res = s[L:R+1]
                resLen = min(resLen, R-L+1)

                window[s[L]] -= 1
                if s[L] in tMap and window[s[L]] < tMap[s[L]]:
                    have -= 1
                
                L += 1
        
        return res
            