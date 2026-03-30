import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(rate):
            i = 0
            for pile in piles:
                i += math.ceil(pile/rate)
            return i <= h

        res = max(piles)
        L, R = 1, res

        while L <= R:
            rate = (L+R)//2
            
            valid = canFinish(rate)

            if valid:
                res = rate
                R = rate - 1
            else:
                L = rate + 1
        
        return res
