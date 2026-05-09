class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            day = 1
            total = 0
            
            for weight in weights:
                if total + weight > capacity:
                    day += 1
                    total = 0
                total += weight
            
            return day <= days
        
        lower, upper = max(weights), sum(weights)

        while lower < upper:
            middle = (lower + upper) // 2

            if canShip(middle):
                upper = middle
            else:
                lower = middle + 1
        
        return upper
