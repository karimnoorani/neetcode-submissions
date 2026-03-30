class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            elif prices[r] > prices[l]:
                profit += prices[r]-prices[l]
                l = r
        
        return profit