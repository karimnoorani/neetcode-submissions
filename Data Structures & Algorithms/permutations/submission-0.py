class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        permutation = []
        res = []
        def backtracking():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            
            for num in nums:
                if num not in visited:
                    permutation.append(num)
                    visited.add(num)
                    backtracking()
                    permutation.pop()
                    visited.remove(num)
        
        backtracking()
        
        return res
