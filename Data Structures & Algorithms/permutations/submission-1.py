class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        chosen = set()
        subset = []

        def dfs():
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for i in range(len(nums)):
                if i not in chosen:
                    chosen.add(i)
                    subset.append(nums[i])
                    dfs()
                    chosen.remove(i)
                    subset.pop()
        
        dfs()
        return res
        