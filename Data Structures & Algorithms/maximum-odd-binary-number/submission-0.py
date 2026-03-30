class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1") - 1
        s = list(s)

        for i in range(len(s)):
            if ones > 0:
                s[i] = "1"
                ones -= 1
            elif i == len(s)-1:
                s[i] = "1"
            else:
                s[i] = "0"
                
        return "".join(s)