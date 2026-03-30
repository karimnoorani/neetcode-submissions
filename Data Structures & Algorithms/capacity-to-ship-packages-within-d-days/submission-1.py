import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(rate):
            ships, curShip = 1, rate
            for w in weights:
                if curShip - w < 0:
                    ships += 1
                    curShip = rate
                curShip -= w
            return ships <= days

        L, R = max(weights), sum(weights)
        res = R

        while L <= R:
            M = (L+R)//2

            if canShip(M):
                R = M - 1
                res = M
            else:
                L = M + 1
        
        return res
