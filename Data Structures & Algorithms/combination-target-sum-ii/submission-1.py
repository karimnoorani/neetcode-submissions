class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(subset[:])
                return
            
            if i >= len(candidates) or total > target:
                return
            
            nextindx = i+1
            while nextindx < len(candidates) and candidates[nextindx] == candidates[i]:
                nextindx += 1
            
            subset.append(candidates[i])
            dfs(i+1, total+candidates[i])
            subset.pop()

            dfs(nextindx, total)

            return
        
        dfs(0, 0)

        return res