class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]

        for i in range(2, len(dp)):
            for j in range(n):
                if i-(j*j) >= 0:
                    dp[i] = min(dp[i], 1+dp[i-(j*j)])
        return dp[-1]