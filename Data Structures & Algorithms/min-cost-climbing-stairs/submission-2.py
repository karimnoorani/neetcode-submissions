class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [c for c in cost]
        for i in range(2, len(dp)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])

            