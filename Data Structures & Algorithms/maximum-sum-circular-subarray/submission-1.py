class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMaxSum = curMinSum = maxSum = minSum = nums[0]
        total = nums[0]

        for n in nums[1:]:
            curMaxSum = max(curMaxSum+n, n)
            curMinSum = min(curMinSum+n, n)

            maxSum = max(maxSum, curMaxSum)
            minSum = min(minSum, curMinSum)

            total += n
        
        if maxSum < 0:
            return maxSum
        
        return max(maxSum, total-minSum)