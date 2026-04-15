class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curSum = 0
        res = 0

        for n in nums:
            curSum += n
            res += prefix[curSum-goal]
            prefix[curSum] += 1
        
        return res
