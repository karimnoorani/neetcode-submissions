import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def dfs(i, subArray):
            if i == len(nums):
                return math.prod(subArray)
            
            stop = math.prod(subArray)
            cont = dfs(i+1, subArray + [nums[i]])
            new = dfs(i+1, [nums[i]])

            return max(stop, cont, new)
        
        return dfs(1, [nums[0]])