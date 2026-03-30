import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            currDays = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    currDays += 1
                    currCap = cap
                currCap -= w
            return currDays <= days
        
        totalSum = sum(weights)
        L, R = max(weights), totalSum
        res = R

        while L <= R:
            M = (L+R)//2

            if canShip(M):
                res = M
                R = M - 1
            else:
                L = M + 1
        
        return res
