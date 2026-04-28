class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
        
        dp = [0 for _ in range(k+maxPts)]
        total = 0
        for i in range(len(dp)-1, k-1, -1):
            dp[i] = 1.0 if i <= n else 0.0
            total += dp[i]
        
        for i in range(k-1, -1, -1):
            dp[i] = total / maxPts
            total -= dp[i+maxPts]
            total += dp[i]
        
        return dp[0]