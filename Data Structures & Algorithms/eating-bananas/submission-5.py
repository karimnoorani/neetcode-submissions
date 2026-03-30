import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = max(piles)

        while L <= R:
            M = (L+R)//2

            hours = 0
            for p in piles:
                hours += math.ceil(p/M)
            
            if hours <= h:
                res = M
                R = M - 1
            else:
                L = M + 1
        
        return res
