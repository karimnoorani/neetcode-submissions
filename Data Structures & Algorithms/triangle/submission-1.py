class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [i for i in triangle[-1]]

        for i in range(len(triangle)-2, -1, -1):
            minPath = [x for x in triangle[i]]
            for j in range(len(minPath)):
                minPath[j] += min(dp[j], dp[j+1])
            dp = minPath
        
        return dp[0]