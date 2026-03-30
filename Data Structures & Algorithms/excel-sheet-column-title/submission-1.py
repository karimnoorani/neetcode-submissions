class Solution:
    def convertToTitle(self, n: int) -> str:
        if n == 0:
            return ""
        
        if n <= 26:
            return chr(n+64)

        return self.convertToTitle(n//26) + chr((n%26)+64)