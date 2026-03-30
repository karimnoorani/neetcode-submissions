class Solution:
    def confusingNumber(self, n: int) -> bool:
        original = n
        rotated = 0
        valid = {0:0, 1:1, 6:9, 8:8, 9:6}

        while n > 0:
            if n % 10 not in valid:
                return False
            rotated = rotated * 10 + valid[n%10]
            n = n // 10
        
        return rotated != original