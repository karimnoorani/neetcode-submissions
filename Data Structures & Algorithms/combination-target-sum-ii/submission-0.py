class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, stack = [], []

        def backtrack(i, currentSum):
            if currentSum == target:
                res.append(stack.copy())
                return
            
            if currentSum > target or i >= len(candidates):
                return
            
            stack.append(candidates[i])
            backtrack(i+1, currentSum + candidates[i])
            stack.pop()

            i = i + 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            
            backtrack(i, currentSum)
        
        backtrack(0, 0)
        return res