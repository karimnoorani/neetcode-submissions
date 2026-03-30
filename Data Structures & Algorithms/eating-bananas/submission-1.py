import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        minK = max(piles)
        
        while low <= high:
            mid = (low+high)//2

            if self.willFinish(piles, mid, h):
                minK = mid
                high = mid-1
            else:
                low = mid + 1
        
        return minK

    def willFinish(self, piles, k, h):
        count = 0
        for num in piles:
            count += math.ceil(num/k)
        return count <= h