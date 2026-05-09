class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        sMap = defaultdict(int)
        L = 0
        count = 0
        res = ""
        for R in range(len(s)):
            sMap[s[R]] += 1
            count += 1 if sMap[s[R]] == tMap.get(s[R], 0) else 0
            while count == len(tMap):
                if res == "" or len(res) > R-L+1:
                    res = s[L:R+1]
                sMap[s[L]] -= 1
                count += -1 if sMap[s[L]] < tMap.get(s[L], 0) else 0
                L += 1
            
        return res