class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        while n > 0:
            bits.append(str(n & 1))
            n = n >> 1
        
        while len(bits) < 32:
            bits.append("0")
        
        return int("".join(bits), 2)