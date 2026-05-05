class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], x[1]))
        dp = [1 for _ in range(len(envelopes))]

        for index in range(len(envelopes)-2, -1, -1):
            for comp_index in range(index+1, len(envelopes)):
                if envelopes[index][0] <  envelopes[comp_index][0] and envelopes[index][1] < envelopes[comp_index][1]:
                    dp[index] = max(dp[index], 1+dp[comp_index])
        
        return max(dp)