class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        chosen = set()
        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for i in range(len(nums)):
                if i not in chosen:
                    chosen.add(i)
                    perm.append(nums[i])
                    dfs()
                    chosen.remove(i)
                    perm.pop()
        
        dfs()
        return res
        