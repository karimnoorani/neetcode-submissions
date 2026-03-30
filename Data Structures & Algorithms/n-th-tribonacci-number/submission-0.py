class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0 if i == 0 else 1 for i in range(n+1)]

        for i in range(3, len(dp)):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

        return dp[-1]
