class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxVal = 0
        for r in range(1, len(prices)):
            maxVal = max(maxVal, prices[r]-prices[l])

            if prices[r] < prices[l]:
                l = r
        
        return maxVal