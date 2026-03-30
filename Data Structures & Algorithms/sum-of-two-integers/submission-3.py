class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        mask = 0xFFFFFFFF
        for i in range(32):
            if a == 0 and b == 0 and carry == 0:
                return res
            
            aBit = a & 1
            bBit = b & 1

            res += (2**i)*(aBit^bBit^carry)
            carry = 1 if [aBit, bBit, carry].count(1) > 1 else 0
            
            a = (a >> 1) & mask
            b = (b >> 1) & mask

        if res > 0x7FFFFFFF:
            res -= 0x100000000

        return res