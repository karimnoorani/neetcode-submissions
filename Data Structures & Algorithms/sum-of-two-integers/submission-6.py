class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        max_int = 0x7FFFFFFF   # 2^31 - 1
        mask = 0xFFFFFFFF
        
        for i in range(32):
            total = (a & 1) + (b & 1) + carry
            res += (total%2)*2**i
            carry = total // 2
            a >>= 1
            b >>= 1
        
        return res if res <= max_int else ~(res ^ mask)
