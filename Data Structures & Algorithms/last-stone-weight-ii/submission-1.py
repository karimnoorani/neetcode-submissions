from math import ceil

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = ceil(sum(stones)/2)
        cache = {i:{} for i in range(len(stones))}
        
        def lastStoneHelper(i, currentSum):
            if currentSum >= target or i == len(stones):
                print(currentSum, sum(stones), target)
                return abs(currentSum - (sum(stones)-currentSum))
            
            if currentSum in cache[i]:
                return cache[i][currentSum]
            
            cache[i][currentSum] = min(lastStoneHelper(i+1, currentSum), lastStoneHelper(i+1, currentSum+stones[i]))

            return cache[i][currentSum]
        
        return lastStoneHelper(0, 0)