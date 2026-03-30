class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def findTargetSumWaysHelper(i, currentSum):
            
            if i >= len(nums):
                if currentSum == target:
                    return 1
                return 0
            
            
            add = findTargetSumWaysHelper(i+1, currentSum+nums[i])
            sub = findTargetSumWaysHelper(i+1, currentSum-nums[i])

            return add + sub
        
        return findTargetSumWaysHelper(0, 0)

