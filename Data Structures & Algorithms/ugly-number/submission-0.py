class Solution:
    def isUgly(self, n: int) -> bool:
        for d in [2, 3, 5]:
            while n % d == 0:
                n = n // d
        return n == 1