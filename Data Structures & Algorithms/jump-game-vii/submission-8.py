class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False

        dp = [False] * (len(s))
        dp[len(s)-1] = True

        for index in range(len(s)-2, -1, -1):
            for jump in range(index+minJump, min(index+maxJump+1, len(s))):
                if s[index] == "0":
                    dp[index] = dp[index] or dp[jump]
        
        return dp[0]