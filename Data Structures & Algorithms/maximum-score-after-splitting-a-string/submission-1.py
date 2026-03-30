class Solution:
    def maxScore(self, s: str) -> int:
        freq = Counter(s)
        freq["0"] = 0

        res = 0
        for c in s[:-1]:
            freq["0"] += 1 if c == '0' else 0
            freq["1"] -= 1 if c == '1' else 0
            res = max(res, freq["0"]+freq["1"])
        
        return res