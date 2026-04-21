class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def satisfies(val):
            total = 0
            for r in ribbons:
                total += math.floor(r/val)
            return total >= k

        L, R = 1, max(ribbons)
        res = 0
        while L <= R:
            M = (L + R) // 2

            if satisfies(M):
                res = M
                L = M + 1
            else:
                R = M - 1
        
        return res