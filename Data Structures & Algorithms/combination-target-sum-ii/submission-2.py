class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(i, total):
            if total == target:
                res.append(subset[:])
                return
            
            if i == len(candidates) or total > target:
                return
            
            subset.append(candidates[i])
            dfs(i+1, total+candidates[i])
            subset.pop()

            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            dfs(i, total)
        
        dfs(0, 0)
        return res