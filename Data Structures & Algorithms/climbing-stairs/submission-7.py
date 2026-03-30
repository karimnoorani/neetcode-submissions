class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
