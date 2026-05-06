class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        perm = []
        res = []
        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    perm.append(nums[i])
                    dfs()
                    used.remove(i)
                    perm.pop()
        dfs()
        return res