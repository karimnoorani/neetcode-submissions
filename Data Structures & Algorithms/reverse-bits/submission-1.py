class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while n > 0:
            res += (n & 1) * (2**(31-i))
            n = n >> 1
            i += 1
        return  res