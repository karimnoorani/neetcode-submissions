class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            res = 0
            for n in nums:
                if i-n >= 0:
                    res += dp[i-n]
            dp[i] = res
        return dp[-1]