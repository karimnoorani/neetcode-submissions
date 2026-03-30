class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        def canPartitionHelper(i, subset1sum, subset2sum):
            if (i, subset1sum, subset2sum) in cache:
                return cache[(i, subset1sum, subset2sum)]

            if i == len(nums):
                return subset1sum == subset2sum
            
            include1 = canPartitionHelper(i+1, subset1sum+nums[i], subset2sum)
            include2 = canPartitionHelper(i+1, subset1sum, subset2sum+nums[i])

            cache[(i, subset1sum, subset2sum)] = include1 or include2
            return cache[(i, subset1sum, subset2sum)]
        
        return canPartitionHelper(0, 0, 0)