class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        cache = {i:{} for i in range(len(nums))}
        def canPartitionHelper(i, target):
            if i == len(nums) or target < 0:
                return False
                
            if target in cache[i]:
                return cache[i][target]
            
            if target == 0:
                return True
            
            
            include = canPartitionHelper(i+1, target-nums[i])
            skip = canPartitionHelper(i+1, target)
            
            cache[i][target] = include or skip

            return cache[i][target]
        
        return canPartitionHelper(0, sum(nums)/2)