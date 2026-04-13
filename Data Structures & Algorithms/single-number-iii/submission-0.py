class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num = 0
        for n in nums:
            num ^= n

        diff_bit = 1
        while not (num & diff_bit):
            diff_bit <<= 1
        
        a = b = 0
        
        for n in nums:
            if n & diff_bit:
                a ^= n
            else:
                b ^= n
        
        return [a, b]