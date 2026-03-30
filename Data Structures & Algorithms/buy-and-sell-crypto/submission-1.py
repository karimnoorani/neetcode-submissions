class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0

        for sell in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[sell]-prices[buy])

            if prices[sell] < prices[buy]:
                buy = sell
        
        return maxProfit