class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def satisfies(sMap):
            for c in tMap:
                if sMap[c] < tMap[c]:
                    return False
            return True
        
        tMap = Counter(t)
        sMap = defaultdict(int)
        L = 0
        res = ""
        for R in range(len(s)):
            sMap[s[R]] += 1

            while satisfies(sMap):
                if res == "" or len(res) > R-L+1:
                    res = s[L:R+1]
                sMap[s[L]] -= 1
                L += 1
        
        return res