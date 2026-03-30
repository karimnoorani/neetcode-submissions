class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        chosen = set()
        res = []
        path = []

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for n in nums:
                if n in chosen:
                    continue
                chosen.add(n)
                path.append(n)
                dfs()
                chosen.remove(n)
                path.pop()
        
        dfs()
        return res