class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x

        while L <= R:
            M = (L+R) // 2

            if M*M > x:
                R = M - 1
            elif M*M < x:
                L = M + 1
            else:
                return M
        
        return min(L, R)