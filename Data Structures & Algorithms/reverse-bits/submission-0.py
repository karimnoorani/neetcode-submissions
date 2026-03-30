class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, '032b')
        res = 0
        for i, c in enumerate(str(n)):
            res += int(c)*(2**i)
        return res