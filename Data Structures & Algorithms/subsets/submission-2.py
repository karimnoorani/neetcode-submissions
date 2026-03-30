class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        subset = []
        def backtrack(i):
            if i >= len(nums):
                return
            
            subset.append(nums[i])
            res.append(subset[:])
            backtrack(i+1)
            
            subset.pop()
            backtrack(i+1)

            return
        
        backtrack(0)

        return res
