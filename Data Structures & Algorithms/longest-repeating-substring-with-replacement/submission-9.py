class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cMap = defaultdict(int)
        L = 0
        res = 0

        for R in range(len(s)):
            cMap[s[R]] += 1

            while (R-L+1)-max(cMap.values()) > k:
                cMap[s[L]] -= 1
                L += 1
            
            res = max(res, R-L+1)
        
        return res