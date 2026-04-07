class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L, R = 1, num

        while L <= R:
            M = (L + R) // 2
            prod = M*M
            if prod > num:
                R = M - 1
            elif prod < num:
                L = M + 1
            else:
                return True
        
        return False