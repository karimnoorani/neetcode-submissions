class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1") - 1
        res = []

        for i in range(len(s)):
            if ones > 0:
                res.append("1")
                ones -= 1
            elif i == len(s)-1:
                res.append("1")
            else:
                res.append("0")
                
        return "".join(res)