class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMaxSum = 0
        maxSum = max(nums)

        curMinSum = 0
        minSum = min(nums)

        for n in nums:
            curMaxSum = max(curMaxSum+n, n)
            curMinSum = min(curMinSum+n, n)

            maxSum = max(maxSum, curMaxSum)
            minSum = min(minSum, curMinSum)
        
        if maxSum < 0:
            return maxSum
        
        return max(maxSum, sum(nums)-minSum)