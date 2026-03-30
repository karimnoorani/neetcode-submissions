class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def canPartitionHelper(i, subset1sum, subset2sum):
            if i == len(nums):
                return subset1sum == subset2sum
            
            include1 = canPartitionHelper(i+1, subset1sum+nums[i], subset2sum)
            include2 = canPartitionHelper(i+1, subset1sum, subset2sum+nums[i])

            return include1 or include2
        
        return canPartitionHelper(0, 0, 0)