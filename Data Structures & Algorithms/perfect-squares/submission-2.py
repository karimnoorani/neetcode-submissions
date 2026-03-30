class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1] = 0, 1

        for i in range(2, len(dp)):
            res = i
            for j in range(i, 0, -1):
                if i-(j*j) >= 0:
                    res = min(res, 1+dp[i-(j*j)])
            dp[i] = res
        print(dp)
        return dp[-1]