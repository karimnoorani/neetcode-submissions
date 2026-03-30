class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {i:{} for i in range(len(nums))}
        def findTargetSumWaysHelper(i, currentSum):
            
            if i >= len(nums):
                if currentSum == target:
                    return 1
                return 0
            
            if currentSum in cache[i]:
                return cache[i][currentSum]
            
            add = findTargetSumWaysHelper(i+1, currentSum+nums[i])
            sub = findTargetSumWaysHelper(i+1, currentSum-nums[i])
            
            cache[i][currentSum] = add + sub

            return cache[i][currentSum]
        
        return findTargetSumWaysHelper(0, 0)

