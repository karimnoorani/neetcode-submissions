class Solution:
    def convertToTitle(self, n: int) -> str:
        if n == 0:
            return ""

        n -= 1
        return self.convertToTitle(n//26) + chr((n%26)+65)